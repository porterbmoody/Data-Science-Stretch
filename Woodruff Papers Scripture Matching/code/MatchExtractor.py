from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import pandas as pd
import subprocess


class MatchExtractor:

    def __init__(self, phrases_woodruff, text_woodruff, threshold: float, path_matches, path_matches_temporary):
        self.threshold = threshold
        self.phrases_woodruff = phrases_woodruff
        self.text_woodruff = text_woodruff
        self.matches_total = pd.DataFrame()
        self.current_matches = pd.DataFrame()
        self.path_matches = path_matches
        self.path_matches_temporary = path_matches_temporary

    def load_vectorizer(self):
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix_woodruff = self.vectorizer.fit_transform(self.phrases_woodruff)

    def run_extractor(self, data_scriptures, save=False, save_temporary=True, publish=False):
        progress_bar = tqdm(total=len(data_scriptures))
        for index, input_row in data_scriptures.iterrows():

            self.tfidf_matrix_woodruff = self.vectorizer.transform(self.phrases_woodruff)
            self.extract_single_phrase_matches(input_row['scripture_text'])
            self.current_matches['verse_title'] = input_row['verse_title']
            self.current_matches['volume_title'] = input_row['volume_title']
            self.current_matches['book_title'] = input_row['book_title']
            self.matches_total = pd.concat([self.matches_total, self.current_matches]).sort_values(
                by='similarity_score', ascending=False)[['phrase_woodruff', 'verse_title', 'similarity_score', 'phrase_scripture', 'volume_title']]

            progress_bar.update(1)
            description = f"{input_row['verse_title']} total match count: {len(self.matches_total)}"
            progress_bar.set_description(description)
            if save_temporary:
                self.matches_total.to_csv(self.path_matches_temporary, index=False)

        progress_bar.close()

        if save:
            self.matches_total.to_csv(self.path_matches, index=False)
        if publish:
            self.quarto_publish()

    def extract_single_phrase_matches(self, phrase_scripture):
        words_woodruff = self.text_woodruff.split()
        words_scripture = phrase_scripture.split()
        # iterate through each n word window the same length as the verse
        for i in range(len(words_woodruff)):
            min = i
            max = i + len(words_scripture)
            if max > len(words_woodruff):
                break
            window_woodruff = " ".join(words_woodruff[min:max])
            print(window_woodruff)



            tfidf_matrix_woodruff = self.vectorizer.transform([window_woodruff])
            tfidf_matrix_scriptures = self.vectorizer.transform([phrase_scripture])
            scores = cosine_similarity(tfidf_matrix_woodruff, tfidf_matrix_scriptures)
            scores = pd.DataFrame(scores, columns=['similarity_score'])
            matches = pd.DataFrame({
                'phrase_woodruff': self.phrases_woodruff,
                'phrase_scripture': phrase_scripture
            })
            self.current_matches = pd.concat([matches, scores], axis=1).query('similarity_score > @self.threshold')
        return

    @staticmethod
    def quarto_publish():
        command = 'quarto publish'
        subprocess.run(command, shell=True, input='y\n', encoding='utf-8')


#%%
string_woodruff = 'hello string of cool words hello my name is bob what is your name my name is pizza'
phrase_scripture = 'keep the commandments hello'

words_woodruff
print(string_woodruff)

def extract_single_phrase_matches(string_woodruff, phrase_scripture):


