from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from StringUtil import StringUtil
from tqdm import tqdm
import pandas as pd
import subprocess


class MatchExtractor:

    def __init__(self, data_woodruff, data_scriptures, phrase_length):
        self.matches_total = pd.DataFrame()
        self.matches_current = pd.DataFrame()
        self.phrase_length = phrase_length
        self.__load_woodruff_data(data_woodruff)
        self.__load_scripture_data(data_scriptures)
        self.__load_vectorizer()

    def __load_woodruff_data(self, data_woodruff):
        self.text_woodruff = StringUtil.combine_rows(data_woodruff['text'])
        # split each verse into a list of phrases then explode it all
        self.phrases_woodruff = StringUtil.split_string_into_list(self.text_woodruff, n = self.phrase_length)

    def __load_vectorizer(self):
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix_woodruff = self.vectorizer.fit_transform(self.phrases_woodruff)

    def __load_scripture_data(self, data_scriptures):
        self.data_scriptures = data_scriptures
        self.data_scriptures['scripture_text'] = self.data_scriptures['scripture_text'].apply(lambda x: StringUtil.split_string_into_list(x, self.phrase_length))
        self.data_scriptures = self.data_scriptures.explode('scripture_text')

    def run_extractor(self, path_matches, path_matches_temporary, threshold: float, save=False, quarto_publish=False):
        self.progress_bar = tqdm(total=len(self.data_scriptures))
        # iterate through each row of data_scriptures_pandas dataframe and run TFIDF vectorizer on the scripture text
        for index, row_scriptures in self.data_scriptures.iterrows():
            self.progress_bar.update(1)
            description = f"{row_scriptures['verse_title']} total match count: {len(self.matches_total)}"
            self.progress_bar.set_description(description)
            # compute cosine similarity scores for given verse
            self.matches_current = self.extract_tfidf_percentage_matches(row_scriptures['scripture_text'])
            self.matches_current['verse_title']  = row_scriptures['verse_title']
            self.matches_current['volume_title'] = row_scriptures['volume_title']
            self.matches_current['book_title']   = row_scriptures['book_title']

            # filter matches by threshold
            self.matches_current = self.matches_current.query("cosine_score > @threshold")
            if len(self.matches_current) > 0:
                self.matches_total = pd.concat([self.matches_total, self.matches_current]).sort_values(
                    by='cosine_score', ascending=False)[['verse_title', 'cosine_score', 'phrase_woodruff','phrase_scripture', 'volume_title']]

                # save to file
                self.matches_total.to_csv(path_matches_temporary, index=False)

        self.progress_bar.close()

        if save:
            self.matches_total.to_csv(path_matches, index=False)
            print(self.matches_total)

        if quarto_publish:
            self.quarto_publish()

    def extract_tfidf_percentage_matches(self, scripture_text):
        tfidf_matrix_scriptures = self.vectorizer.transform([scripture_text])
        cosine_scores = cosine_similarity(self.tfidf_matrix_woodruff, tfidf_matrix_scriptures)
        cosine_scores = pd.DataFrame(cosine_scores, columns=['cosine_score'])
        cosine_scores['phrase_woodruff'] = self.phrases_woodruff
        cosine_scores['phrase_scripture'] = scripture_text
        return cosine_scores

    @staticmethod
    def quarto_publish():
        command = 'quarto publish'
        subprocess.run(command, shell = True, input = 'y\n', encoding = 'utf-8')

#%%
