from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import subprocess



class MatchExtractor:

    def __init__(self, phrases_woodruff, threshold, path_matches) -> None:
        self.threshold = threshold
        self.phrases_woodruff = phrases_woodruff
        self.total_matches = pd.DataFrame()
        self.current_matches = pd.DataFrame()
        self.path_matches = path_matches
        self.__load_vectorizer()

    def __load_vectorizer(self):
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix_1 = self.vectorizer.fit_transform(self.phrases_woodruff)

    def extract_matches_phrase(self, scripure_kwargs, save = False):
        """ pass in list with single string scripture phrase and it
            returns matches dataframe
        """

        tfidf_matrix_2 = self.vectorizer.transform([scripure_kwargs['scripture_text']])

        # returns a matrix of similarity scores
        scores = cosine_similarity(self.tfidf_matrix_1, tfidf_matrix_2)
        # merge scores in with their respective phrases
        scores = pd.DataFrame(scores, columns = ['similarity_score'])

        matches = pd.DataFrame({
            'phrase_woodruff' : self.phrases_woodruff,
            'phrase_scripture' : scripure_kwargs['scripture_text']
            })

        self.current_matches = pd.concat([matches, scores], axis=1).query('similarity_score > @self.threshold')
        self.current_matches['volume_title'] = scripure_kwargs['volume_title']
        self.current_matches['book_title'] = scripure_kwargs['book_title']
        self.current_matches['verse_title'] = scripure_kwargs['verse_title']
        self.total_matches = pd.concat([self.total_matches, self.current_matches]).sort_values(by = 'similarity_score', ascending=False)
        if save:
            self.save_matches()

    def save_matches(self):
        self.total_matches.to_csv(self.path_matches, index=False)

    @staticmethod
    def quarto_publish():
        command = 'quarto publish'
        # Run the command and automatically provide "y" as input
        subprocess.run(command, shell=True, input='y\n', encoding='utf-8')