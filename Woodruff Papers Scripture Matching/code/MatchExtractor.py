from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import pandas as pd
import subprocess


class MatchExtractor:
    def __init__(self, phrases_woodruff, threshold: float, path_matches, path_matches_temporary):
        self.threshold = threshold
        self.phrases_woodruff = phrases_woodruff
        self.matches_total = pd.DataFrame()
        self.current_matches = pd.DataFrame()
        self.path_matches = path_matches
        self.path_matches_temporary = path_matches_temporary
        self.load_vectorizer()

    def load_vectorizer(self):
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix_1 = self.vectorizer.fit_transform(self.phrases_woodruff)

    def run_extractor(self, data_input, save=False, save_temporary=True, publish=False):
        self.progress_bar = tqdm(total=len(data_input))
        for index, input_row in data_input.iterrows():
            self.extract_single_phrase_matches(input_row['scripture_text'])
            self.current_matches['verse_title'] = input_row['verse_title']
            self.current_matches['volume_title'] = input_row['volume_title']
            self.current_matches['book_title'] = input_row['book_title']
            self.matches_total = pd.concat([self.matches_total, self.current_matches]).sort_values(
                by='similarity_score', ascending=False)

            self.progress_bar.update(1)
            description = f"{input_row['verse_title']} total match count: {len(self.matches_total)}"
            self.progress_bar.set_description(description)
            if save_temporary:
                self.matches_total.to_csv(self.path_matches_temporary, index=False)

        self.progress_bar.close()

        if save:
            self.matches_total.to_csv(self.path_matches, index=False)
        if publish:
            self.quarto_publish()

    def extract_single_phrase_matches(self, phrase):
        tfidf_matrix_2 = self.vectorizer.transform([phrase])
        scores = cosine_similarity(self.tfidf_matrix_1, tfidf_matrix_2)
        scores = pd.DataFrame(scores, columns=['similarity_score'])
        matches = pd.DataFrame({
            'phrase_woodruff': self.phrases_woodruff,
            'phrase_scripture': phrase
        })
        self.current_matches = pd.concat([matches, scores], axis=1).query('similarity_score > @self.threshold')

    @staticmethod
    def quarto_publish():
        command = 'quarto publish'
        subprocess.run(command, shell=True, input='y\n', encoding='utf-8')
