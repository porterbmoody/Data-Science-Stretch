from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import pandas as pd
import subprocess


class MatchExtractor:
    """ class for implementing TFIDF vectorizer efficiently and concisely
        initialize with list of strings that the vectorizer trains on, a percentage threshold
        some functions specicifically tailored towards woodruff and scripture data at the moment which is not idea.
    """

    def __init__(self, phrases_woodruff, threshold: float, path_matches, path_matches_temporary) -> None:
        self.threshold = threshold
        self.phrases_woodruff = phrases_woodruff
        self.total_matches = pd.DataFrame()
        self.current_matches = pd.DataFrame()
        self.path_matches = path_matches
        self.path_matches_temporary = path_matches_temporary
        self.__load_vectorizer()

    def __load_vectorizer(self):
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix_1 = self.vectorizer.fit_transform(self.phrases_woodruff)

    def run_extractor(self, data_input, save = False, publish = False):
        """ iterate through each row in data_input pandas dataframe
            and run TFIDF vectorizer and cosine similarity against each input phrase
        """
        self.progress_bar = tqdm(total=len(data_input))
        # iterate through each row of scripture phrases dataset and run TFIDF model and cosine similarity.
        for index, input_row in data_input.iterrows():
            self.input_row = input_row
            self._extract_single_phrase_matches()
            self.progress_bar.update(1)
            description = input_row['verse_title'] + ' total match count: ' + str(len(self.total_matches))# + 'verse length: ' + str(len(phrases_scriptures[0]))
            self.progress_bar.set_description(description)

        self.progress_bar.close()

        if save:
            self.total_matches.to_csv(self.path_matches, index=False)
        if publish:
            self.quarto_publish()

    def _extract_single_phrase_matches(self):
        """ pass in list with single string scripture phrase and it
            returns matches dataframe
        """
        tfidf_matrix_2 = self.vectorizer.transform([self.input_row['scripture_text']])
        # returns a matrix of similarity scores
        scores = cosine_similarity(self.tfidf_matrix_1, tfidf_matrix_2)
        # merge scores in with their respective phrases
        scores = pd.DataFrame(scores, columns = ['similarity_score'])

        matches = pd.DataFrame({
            'phrase_woodruff' : self.phrases_woodruff,
            'phrase_scripture' : self.input_row['scripture_text']
            })
        self.current_matches = pd.concat([matches, scores], axis=1).query('similarity_score > @self.threshold')
        self.current_matches['volume_title'] = self.input_row['volume_title']
        self.current_matches['book_title']   = self.input_row['book_title']
        self.current_matches['verse_title']  = self.input_row['verse_title']
        self.total_matches = pd.concat([self.total_matches, self.current_matches]).sort_values(by = 'similarity_score', ascending=False)
        # save current matches to temporary location
        self.total_matches.to_csv(self.path_matches_temporary, index = False)

    @staticmethod
    def quarto_publish():
        command = 'quarto publish'
        # Run the command and automatically provide "y" as input
        subprocess.run(command, shell=True, input='y\n', encoding='utf-8')