from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from StringUtil import StringUtil
from tqdm import tqdm
import pandas as pd
import subprocess

class MatchExtractor:
    """ match extractor class, pass initialize with 2 pandas dataframes and the phrase to split each row of text into
    """

    def __init__(self, data_woodruff, data_scriptures, phrase_length):
        self.matches_total = pd.DataFrame()
        self.matches_current = pd.DataFrame()
        self.phrase_length = phrase_length
        self.__load_woodruff_data(data_woodruff)
        self.__load_scripture_data(data_scriptures)
        self.__load_vectorizer()

    def __load_woodruff_data(self, data_woodruff):
        """ save self.data_woodruff as pandas dataframe
        """
        # split each journal entry into a list of phrases then explode it all
        self.data_woodruff = StringUtil.expand_dataframe_of_text(data_woodruff, 'text', self.phrase_length)

    def __load_scripture_data(self, data_scriptures):
        """ save self.data_scripture as pandas dataframe
        """
        # split each verse into a list of phrases then explode it all
        self.data_scriptures = StringUtil.expand_dataframe_of_text(data_scriptures, 'text', self.phrase_length)

    def __load_vectorizer(self):
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix_woodruff = self.vectorizer.fit_transform(self.data_woodruff['text'])

    def run_extractor(self, path_matches, path_matches_temporary, threshold: float, save = False, quarto_publish = False):
        """ Iterate through each row of expanded scriptures dataframe and run extract_tfidf_percentage_matches method on the single phrase
            then attach verse columns to current match dataframe
            then filter down to only matches of a certain threshold
            the conditionally save or publish to quarto
        """
        self.progress_bar = tqdm(total=len(self.data_scriptures) - 1)
        # index_scriptures = 0
        # index_woodruff = 0
        index_match_references = []
        # print("length scripture;", len(self.data_scriptures) - 1)
        # print("length woodruff;", len(self.data_woodruff) - 1)
        # iterate through each row of data_scriptures_pandas dataframe and run TFIDF vectorizer on the scripture text
        for index_scriptures, row_scriptures in self.data_scriptures.iterrows():
            self.progress_bar.update(1)
            description = f"{row_scriptures['verse_title']} total match count: {len(self.matches_total)}"
            self.progress_bar.set_description(description)
            for index_woodruff, row_woodruff in self.data_woodruff.iterrows():
            # row_scriptures = self.data_scriptures.iloc[index_scriptures]
        # while index_scriptures < len(self.data_scriptures) - 1:
        #     while index_woodruff < len(self.data_woodruff) - 1:
                # row_woodruff = self.data_woodruff.iloc[index_woodruff]
                phrase_woodruff = row_woodruff['text']
                phrase_scriptures = row_scriptures['text']
                verse_title = row_scriptures['verse_title']
                date = row_woodruff['date']
                cosine_score = self.compute_similarity(phrase_woodruff, phrase_scriptures)
                if cosine_score > threshold:
                    match_indices = (index_woodruff, index_scriptures)
                    if match_indices in index_match_references:
                        # print("POOOOOOOOOOOOOOOOOOOOOP")
                        # print('repeat matches...', match_indices)
                        continue
                    index_match_references.append(match_indices)
                    # print('current indices:', match_indices)
                    # print('all indices:', index_match_references)
                    index_woodruff_extension = index_woodruff
                    index_scriptures_extension = index_scriptures
                    valid = True
                    while valid:
                        # add next phrase to the end of current phrase then compute cosine similarity on the new extended phrase
                        index_woodruff_extension   += 1
                        index_scriptures_extension += 1
                        match_indices = (index_woodruff_extension, index_scriptures_extension)
                        # if match_indices in index_match_references:
                            # break
                        if index_woodruff_extension >= len(self.data_woodruff):
                            break
                        if index_scriptures_extension >= len(self.data_scriptures):
                            break
                        # print('current extension indices:', match_indices)
                        # print('all indices:', index_match_references)
                        # print('='*50)
                        # print('extending...')
                        phrase_extension_woodruff   = self.data_woodruff.iloc[index_woodruff_extension]['text']
                        phrase_extension_scriptures = self.data_scriptures.iloc[index_scriptures_extension]['text']
                        # print(phrase_extension_woodruff)
                        # print(phrase_extension_scriptures)
                        cosine_score = self.compute_similarity(phrase_extension_woodruff, phrase_extension_scriptures)
                        if cosine_score > threshold:
                            # append extension indices to list of all match indices
                            index_match_references.append(match_indices)
                            phrase_woodruff   += " " + phrase_extension_woodruff
                            phrase_scriptures += " " + phrase_extension_scriptures
                            print(phrase_woodruff)
                            print(phrase_woodruff)
                            print('score:', cosine_score)
                        else:
                            cosine_score = self.compute_similarity(phrase_woodruff, phrase_scriptures)
                            break

                    match_found_dataframe = pd.DataFrame({
                        'date'             : date,
                        'phrase_woodruff'  : phrase_woodruff,
                        'phrase_scripture' : phrase_scriptures,
                        'verse_title'      : verse_title,
                        'cosine_score'     : cosine_score,
                    }, index = [0])
                    # print(match_found)
                    if len(match_found_dataframe) > 0:
                        self.matches_total = pd.concat([self.matches_total, match_found_dataframe]).sort_values(
                            by='cosine_score', ascending=False)[['date', 'verse_title', 'cosine_score', 'phrase_woodruff','phrase_scripture']]

                # filter matches by threshold
                # self.matches_current = self.matches_current.query("cosine_score > @threshold")
                index_woodruff += 1
            index_scriptures += 1

            # save to file
            self.matches_total.to_csv(path_matches_temporary, index=False)
        # for index, row_scriptures in self.data_scriptures.iterrows():
        #     # compute cosine similarity scores for given verse
        #     self.matches_current = self.extract_tfidf_percentage_matches(row_scriptures['text'])
        #     self.matches_current['verse_title']  = row_scriptures['verse_title']
        #     self.matches_current['volume_title'] = row_scriptures['volume_title']

        self.progress_bar.close()

        if save:
            self.matches_total.to_csv(path_matches, index=False)
            print(self.matches_total)

        if quarto_publish:
            self.quarto_publish()

    def compute_similarity(self, text_woodruff, text_scripture):
        raw_percentage_match = StringUtil.str_percentage_match(text_woodruff, text_scripture)
        if raw_percentage_match > 0.1:
            tfidf_matrix_woodruff = self.vectorizer.transform([text_woodruff])
            tfidf_matrix_scriptures = self.vectorizer.transform([text_scripture])
            cosine_score = cosine_similarity(tfidf_matrix_woodruff, tfidf_matrix_scriptures)[0][0]
            # cosine_scores = pd.DataFrame(cosine_scores, columns=['cosine_score'])
            return round(cosine_score, 5)
        else:
            return 0

    # def extract_tfidf_percentage_matches(self, scripture_text):
    #     tfidf_matrix_scriptures = self.vectorizer.transform([scripture_text])
    #     cosine_scores = cosine_similarity(self.tfidf_matrix_woodruff, tfidf_matrix_scriptures)
    #     cosine_scores = pd.DataFrame(cosine_scores, columns=['cosine_score']).apply(lambda x: round(x, 5))
    #     cosine_scores['phrase_woodruff'] = list(self.data_woodruff['text'])
    #     cosine_scores['date'] = list(self.data_woodruff['date'])
    #     cosine_scores['phrase_scripture'] = scripture_text
    #     return cosine_scores

    @staticmethod
    def quarto_publish():
        command = 'quarto publish'
        subprocess.run(command, shell = True, input = 'y\n', encoding = 'utf-8')

#%%
