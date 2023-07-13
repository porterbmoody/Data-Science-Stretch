from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from StringUtil import StringUtil
from tqdm import tqdm
import itertools
import pandas as pd
import subprocess



class MatchExtractor:
    """ match extractor class, pass initialize with 2 pandas dataframes and the phrase to split each row of text into
    """

    def __init__(self, data_woodruff, data_scriptures, phrase_length, threshold):
        self.matches_total = pd.DataFrame()
        self.matches_current = pd.DataFrame()
        self.phrase_length = phrase_length
        self.threshold = threshold
        self.path_matches             = '../data/matches/data_matches.csv'
        self.path_matches_temporary   = '../data/matches/data_matches_temporary.csv'
        self.path_matches_extensions = '../data/matches/data_matches_extensions.csv'
        self.path_matches_extensions_temporary = '../data/matches/data_matches_extensions_temporary.csv'
        # local paths
        self.__load_woodruff_data(data_woodruff)
        self.__load_scripture_data(data_scriptures)
        self.__load_vectorizer()

    def __load_woodruff_data(self, data_woodruff):
        """ save self.data_woodruff as pandas dataframe
        """
        self.data_woodruff_full = data_woodruff.copy()
        # split each journal entry into a list of phrases then explode it all
        self.data_woodruff = StringUtil.expand_dataframe_of_text(data_woodruff, 'text', self.phrase_length)

    def __load_scripture_data(self, data_scriptures):
        """ save self.data_scripture as pandas dataframe
        """
        self.data_scriptures_full = data_scriptures.copy()
        # split each verse into a list of phrases then explode it all
        self.data_scriptures = StringUtil.expand_dataframe_of_text(data_scriptures, 'text', self.phrase_length)

    def __load_vectorizer(self):
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix_woodruff = self.vectorizer.fit_transform(self.data_woodruff['text'])

    def run_extractor(self, save = False, quarto_publish = False):
        """ Uses already trained TFIDF model, first extraction algorithm
            loops through each row of expanded scriptures dataframe and computes the tfidf vector of each scriptures phrase
            then compute the vectors of each woodruff phrase and create a vector
            then compute cosine similarity between each vector and filter by a certain threshold.
            then append everything back into a dataset.
        """
        self.progress_bar = tqdm(total=len(self.data_scriptures))
        # iterate through each row of data_scriptures_pandas dataframe and run TFIDF vectorizer on the scripture text
        for index, row_scriptures in self.data_scriptures.iterrows():
            self.progress_bar.update(1)
            description = f"{row_scriptures['verse_title']} total match count: {len(self.matches_total)}"
            self.progress_bar.set_description(description)
            # compute cosine similarity scores for given verse
            self.compute_percentage_matches(row_scriptures['text'])
            self.matches_current['index_scriptures'] = index
            self.matches_current['verse_title']  = row_scriptures['verse_title']
            self.matches_current['volume_title'] = row_scriptures['volume_title']
            self.matches_current['book_title']   = row_scriptures['book_title']
            # filter matches by threshold
            self.matches_current = self.matches_current.query("cosine_score > @self.threshold")
            if len(self.matches_current) > 0:
                self.matches_total = pd.concat([self.matches_total, self.matches_current]).sort_values(
                    by=['index_woodruff', 'index_scriptures'], ascending=True)

                # save to file
                self.resolve_extensions()
                self.matches_total.sort_values(by='cosine_score', ascending=False).to_csv(self.path_matches, index=False)

        self.progress_bar.close()

        # if save:
            # self.matches_total.sort_values(by='cosine_score', ascending=False)#.to_csv(self.path_matches, index=False)
            # self.matches_extensions.to_csv(self.path_matches_extensions, index = False)

        if quarto_publish:
            self.quarto_publish()

    def compute_percentage_matches(self, scripture_text):
        """ Pass in a single string and it returns a pandas dataframe containing the woodruff phrases along with the cosine similarity value
        """
        tfidf_matrix_scriptures = self.vectorizer.transform([scripture_text])
        cosine_scores = cosine_similarity(self.tfidf_matrix_woodruff, tfidf_matrix_scriptures)
        cosine_scores = pd.DataFrame(cosine_scores, columns=['cosine_score'])
        cosine_scores['cosine_score'] = cosine_scores['cosine_score'].apply(lambda x: round(x, 5))
        cosine_scores['phrase_woodruff'] = list(self.data_woodruff['text'])
        cosine_scores['date'] = list(self.data_woodruff['date'])
        cosine_scores['phrase_scripture'] = scripture_text
        self.matches_current = cosine_scores.rename_axis('index_woodruff').reset_index()

    def resolve_extensions(self):
        """ Use indices to attaches matching phrases that go right next to each other
        """
        self.matches_total.sort_values(['index_woodruff', 'index_scriptures'], inplace=True)
        # Create a mask to identify rows where the indices are not 1 apart
        mask = (self.matches_total['index_woodruff'].diff() != 1) | (self.matches_total['index_scriptures'].diff() != 1)
        # Create a new column to identify groups based on the mask
        self.matches_total['group'] = mask.cumsum()
        self.matches_total = self.matches_total.groupby('group').agg({
            'index_woodruff': 'first',
            'index_scriptures': 'first',
            # 'match_count' : 'sum',
            'date': 'first',
            'cosine_score': 'mean',
            'verse_title': 'first',
            'volume_title': 'first',
            'phrase_woodruff': ' '.join,
            'phrase_scripture': ' '.join,
        })
        # print(self.matches_total)

    @staticmethod
    def quarto_publish():
        command = 'quarto publish'
        subprocess.run(command, shell = True, input = 'y\n', encoding = 'utf-8')

#%%
