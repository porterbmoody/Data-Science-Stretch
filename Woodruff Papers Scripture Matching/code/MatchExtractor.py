from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from DataUtil import DataUtil
from tqdm import tqdm
import pandas as pd
import subprocess


class MatchExtractor:

    def __init__(self, text_woodruff, threshold: float, phrase_length, path_matches: str):
        self.threshold = threshold
        self.matches_total = pd.DataFrame()
        self.matches_current = pd.DataFrame()
        self.path_matches = path_matches
        self.phrase_length = phrase_length
        self.path_matches_temporary = 'Woodruff Papers Scripture Matching/data/data_matches.csv'
        self.load_woodruff_data(text_woodruff)
        self.load_vectorizer()

    def load_woodruff_data(self, text_woodruff):
        self.text_woodruff = text_woodruff
        # split each verse into a list of phrases then explode it all
        self.phrases_woodruff = DataUtil.split_string_into_list(self.text_woodruff, n = self.phrase_length)

    def load_vectorizer(self):
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix_woodruff = self.vectorizer.fit_transform(self.phrases_woodruff)

    def run_extractor(self, data_scriptures, save=False, save_temporary=True, publish=False):
        self.progress_bar = tqdm(total=len(data_scriptures))
        for index, row_scriptures in data_scriptures.iterrows():
            self.progress_bar.update(1)
            description = f"{row_scriptures['verse_title']} total match count: {len(self.matches_total)}"
            self.progress_bar.set_description(description)
            # print(row_scriptures)
            # initial filter to get out very low percentage matches
            self.extract_tfidf_percentage_matches(row_scriptures)
            # secondary filter to remove low tfidf percentage matches
            # self.matches_current = self.compute_tfidf_percentage_match(row['scripture_text'])
            # self.extract_single_phrase_matches(row['scripture_text'])
            # print(self.matches_current)
            if len(self.matches_current) > 0:
                self.matches_total = pd.concat([self.matches_total, self.matches_current]).sort_values(
                    by='cosine_score', ascending=False)[['verse_title', 'cosine_score', 'phrase_woodruff','phrase_scripture', 'volume_title']]

                # save to file
                self.matches_total.to_csv(self.path_matches_temporary, index=False)

        self.progress_bar.close()

        if save:
            self.matches_total.to_csv(self.path_matches, index=False)
            print(self.matches_total)

        if publish:
            self.quarto_publish()

    # def extract_tfidf_percentage_matches(self, phrase_scripture):

    def extract_tfidf_percentage_matches(self, row_scriptures):
        # self.matches_current = pd.concat([matches, scores], axis=1).query('similarity_score > @self.threshold')
        # tfidf_matrix_woodruff = self.vectorizer.transform(phrases_woodruff)
        tfidf_matrix_scriptures = self.vectorizer.transform([row_scriptures['scripture_text']])
        cosine_scores = cosine_similarity(self.tfidf_matrix_woodruff, tfidf_matrix_scriptures)
        cosine_scores = pd.DataFrame(cosine_scores, columns=['cosine_score'])
        # print(cosine_scores)
        cosine_scores['phrase_woodruff'] = self.phrases_woodruff
        cosine_scores['phrase_scripture'] = row_scriptures['scripture_text']

        self.matches_current = cosine_scores
        self.matches_current['verse_title']  = row_scriptures['verse_title']
        self.matches_current['volume_title'] = row_scriptures['volume_title']
        self.matches_current['book_title']   = row_scriptures['book_title']
        self.matches_current = self.matches_current.query("cosine_score > @self.threshold")
        # return round(cosine_score[0][0], 4)
        # matches = pd.DataFrame({
        #     'phrase_woodruff' :self.phrases_woodruff,
        #     'phrase_scripture':phrase_scripture,
        #     })

    # def compute_string_match_percentages_window(self, phrase_scripture):
    #     words_woodruff = self.text_woodruff.split()
    #     words_scripture = phrase_scripture.split()
    #     percentage_match_list = []
    #     window_list = []
    #     phrase_scripture_list = []
    #     # iterate through each n word window the same length as the verse
    #     for i in range(0, len(words_woodruff), 10):
    #         min = i
    #         max = i + len(words_scripture)
    #         if max > len(words_woodruff):
    #             break
    #         window_woodruff = " ".join(words_woodruff[min:max])
    #         # print('comparing...')
    #         # print(window)
    #         # print(string2)
    #         percentage_match_raw = DataUtil.string_percentage_match(window_woodruff, phrase_scripture)
    #         # raw percentage match filter
    #         if percentage_match_raw > .2:
    #             percentage_match_idfidf = self.compute_tfidf_percentage_match(window_woodruff, phrase_scripture)
    #             # tfidf percentage match filter
    #             if percentage_match_idfidf > self.threshold:
    #                 percentage_match_list.append(percentage_match_idfidf)
    #                 window_list.append(window_woodruff)
    #                 phrase_scripture_list.append(phrase_scripture)
    #     matches = pd.DataFrame({
    #         'phrase_woodruff' : window_list,
    #         'phrase_scripture' : phrase_scripture_list,
    #         'percentage_match' : percentage_match_list,
    #         })
    #     self.matches_current = matches.sort_values(by = 'percentage_match', ascending=False)

    # def compute_scripture_match_percentages(self, phrase_scripture):
    #     percentage_match_list = []
    #     phrase_woodruff_list = []
    #     phrase_scripture_list = []
    #     for phrase_woodruff in self.phrases_woodruff:
    #         # percentage_match_raw = DataUtil.string_percentage_match(phrase_woodruff, phrase_scripture)
    #         print('comparing...')
    #         print(phrase_woodruff)
    #         print(phrase_scripture)
    #         # # raw percentage match filter
    #         # if percentage_match_raw > .1:
    #         percentage_match_idfidf = self.compute_tfidf_percentage_match(phrase_woodruff, phrase_scripture)
    #         # tfidf percentage match filter
    #         if percentage_match_idfidf > self.threshold:
    #             percentage_match_list.append(percentage_match_idfidf)
    #             phrase_woodruff_list.append(phrase_woodruff)
    #             phrase_scripture_list.append(phrase_scripture)
    #     matches = pd.DataFrame({
    #         'phrase_woodruff'  : phrase_woodruff_list,
    #         'phrase_scripture' : phrase_scripture_list,
    #         'cosine_score' : percentage_match_list,
    #         })
    #     self.matches_current = matches.sort_values(by = 'cosine_score', ascending=False)



    @staticmethod
    def quarto_publish():
        command = 'quarto publish'
        subprocess.run(command, shell=True, input='y\n', encoding='utf-8')


#%%
# string_woodruff = 'hello string of cool words hello my name is bob what is your name my name is pizza'
# phrase_scripture = 'keep the commandments hello'
# words_woodruff = string_woodruff.split()
# words_scripture = phrase_scripture.split()

# print('running looping window...\n')

# for i in range(len(words_woodruff)):
#     min = i
#     max = i + len(words_scripture)
#     if max > len(words_woodruff):
#         break
#     window_woodruff = " ".join(words_woodruff[min:max])
#     print('comparing...', window_woodruff,'\n', phrase_scripture)



