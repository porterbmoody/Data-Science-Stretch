from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from StringUtil import StringUtil
from tqdm import tqdm
import pandas as pd
import subprocess


class MatchExtractor:
    """ match extractor class, pass initialize with 2 pandas dataframes and the phrase to split each row of text into
    """

    def __init__(self, data_woodruff, data_scriptures, phrase_length, threshold):
        self.path_matches             = '../data/data_matches.csv'
        self.path_matches_temporary   = '../data/data_matches_temporary.csv'
        self.path_matches_extensions = '../data/data_matches_extensions.csv'
        self.path_matches_extensions_temporary = '../data/data_matches_extensions_temporary.csv'
        self.matches_total = pd.DataFrame()
        self.matches_current = pd.DataFrame()
        self.phrase_length = phrase_length
        self.threshold = threshold
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

    def run_extractor(self, save=False, quarto_publish=False):
        self.progress_bar = tqdm(total=len(self.data_scriptures))
        # iterate through each row of data_scriptures_pandas dataframe and run TFIDF vectorizer on the scripture text
        for index, row_scriptures in self.data_scriptures.iterrows():
            self.progress_bar.update(1)
            description = f"{row_scriptures['verse_title']} total match count: {len(self.matches_total)}"
            self.progress_bar.set_description(description)
            # compute cosine similarity scores for given verse
            self.matches_current = self.extract_tfidf_percentage_matches(row_scriptures['text'])
            self.matches_current['verse_title']  = row_scriptures['verse_title']
            self.matches_current['volume_title'] = row_scriptures['volume_title']
            self.matches_current['book_title']   = row_scriptures['book_title']

            # filter matches by threshold
            self.matches_current = self.matches_current.query("cosine_score > @self.threshold")
            if len(self.matches_current) > 0:
                self.matches_total = pd.concat([self.matches_total, self.matches_current]).sort_values(
                    by='cosine_score', ascending=False)[['date', 'verse_title', 'cosine_score', 'phrase_woodruff','phrase_scripture', 'volume_title']]

                # save to file
                self.matches_total.to_csv(self.path_matches_temporary, index=False)

        self.progress_bar.close()

        if save:
            self.matches_total.to_csv(self.path_matches, index=False)
            print(self.matches_total)

        if quarto_publish:
            self.quarto_publish()

    def __load_extensions_data(self):
        # filter input data down to rows that already contain matches
        if not len(self.matches_total) > 0:
            self.matches_total =  pd.read_csv(self.path_matches_temporary)
        date_matches = list(self.matches_total['date'].unique())
        self.data_woodruff_filtered = self.data_woodruff.query('date in @date_matches')[['date','text']]

        verse_matches = list(self.matches_total['verse_title'].unique())
        self.data_scriptures_filtered = self.data_scriptures.query('verse_title in @verse_matches')

    def extract_extensions(self, save = False, quarto_publish = False):
        """ Iterate through each row of expanded scriptures dataframe as well as each row of expanded woodruff dataframe that both only contain verses where a match has already been found
            run extract_tfidf_percentage_matches method on the single phrase
            then filter down to only matches of a certain threshold
            the conditionally save or publish to quarto
        """
        self.__load_extensions_data()
        self.text1_list = self.data_woodruff_filtered['text']
        self.text2_list = self.data_scriptures_filtered['text']
        # print(text1_list)
        # print(text2_list)
        self.matches_extensions = StringUtil.extract_matches_extensions(
            self.vectorizer, list(self.text1_list),
            list(self.text2_list),
            threshold = self.threshold,
            path_temporary = self.path_matches_extensions_temporary)

        self.matches_extensions.to_csv(self.path_matches_extensions_temporary)

        if save:
            self.matches_extensions.to_csv(self.path_matches_extensions, index=False)
            print(self.matches_extensions)

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

    def extract_tfidf_percentage_matches(self, scripture_text):
        tfidf_matrix_scriptures = self.vectorizer.transform([scripture_text])
        cosine_scores = cosine_similarity(self.tfidf_matrix_woodruff, tfidf_matrix_scriptures)
        cosine_scores = pd.DataFrame(cosine_scores, columns=['cosine_score']).apply(lambda x: round(x, 5))
        cosine_scores['phrase_woodruff'] = list(self.data_woodruff['text'])
        cosine_scores['date'] = list(self.data_woodruff['date'])
        cosine_scores['phrase_scripture'] = scripture_text
        return cosine_scores

    @staticmethod
    def quarto_publish():
        command = 'quarto publish'
        subprocess.run(command, shell = True, input = 'y\n', encoding = 'utf-8')

#%%
        # self.progress_bar = tqdm(total=len(self.data_scriptures_filtered) - 1)
        # index_match_references = []
        # # iterate through each row of data_scriptures_pandas dataframe and run TFIDF vectorizer on the scripture text
        # for index_scriptures, row_scriptures in self.data_scriptures_filtered.iterrows():
        #     self.progress_bar.update(1)
        #     description = f"{row_scriptures['verse_title']} total match count: {len(self.matches_total)}"
        #     self.progress_bar.set_description(description)
        #     phrase_scriptures = row_scriptures['text']
        #     verse_title = row_scriptures['verse_title']
        #     for index_woodruff, row_woodruff in self.data_woodruff_filtered.iterrows():
        #         match_indices = (index_woodruff, index_scriptures)
        #         if match_indices in index_match_references: # if match has already been found, the indices should be stored in references list
        #             print('repeat matches...', match_indices)
        #             continue
        #         index_match_references.append(match_indices)
        #         phrase_woodruff = row_woodruff['text']
        #         date = row_woodruff['date']
        #         cosine_score = self.compute_similarity(phrase_woodruff, phrase_scriptures)
        #         if cosine_score > self.threshold: # match found
        #             index_woodruff_extension   = index_woodruff
        #             index_scriptures_extension = index_scriptures
        #             while True:
        #                 # add next phrase to the end of current phrase then compute cosine similarity on the new extended phrase
        #                 index_woodruff_extension   += 1
        #                 index_scriptures_extension += 1
        #                 match_indices = (index_woodruff_extension, index_scriptures_extension)
        #                 if match_indices in index_match_references:
        #                     print('repeat matches...', match_indices)
        #                     break
        #                 if index_woodruff_extension >= len(self.data_woodruff_filtered):
        #                     break
        #                 if index_scriptures_extension >= len(self.data_scriptures_filtered):
        #                     break
        #                 phrase_extension_woodruff   = self.data_woodruff_filtered.iloc[index_woodruff_extension]['text']
        #                 phrase_extension_scriptures = self.data_scriptures_filtered.iloc[index_scriptures_extension]['text']
        #                 cosine_score = self.compute_similarity(phrase_extension_woodruff, phrase_extension_scriptures)
        #                 index_match_references.append(match_indices)
        #                 if cosine_score > self.threshold:
        #                     print('extension match found...')
        #                     print(phrase_extension_woodruff)
        #                     # append extension indices to list of all match indices
        #                     phrase_woodruff   += " " + phrase_extension_woodruff
        #                     phrase_scriptures += " " + phrase_extension_scriptures
        #                 else:
        #                     cosine_score = self.compute_similarity(phrase_woodruff, phrase_scriptures)
        #                     break

                # if len(matches_extensions) > 0:
            # self.matches_total = pd.concat([self.matches_total, match_found_dataframe]).sort_values(
                # by='cosine_score', ascending=False)[['date', 'verse_title', 'cosine_score', 'phrase_woodruff','phrase_scripture']]

            #     # filter matches by threshold
            #     self.matches_current = self.matches_current.query("cosine_score > @self.threshold")
            #     index_woodruff += 1
            # index_scriptures += 1

        #     # save to file
            # self.matches_total.to_csv(self.path_matches_extensions_temporary, index=False)