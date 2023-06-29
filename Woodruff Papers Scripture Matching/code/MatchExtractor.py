from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from DataUtil import DataUtil
from tqdm import tqdm
import pandas as pd
import subprocess


class MatchExtractor:

    def __init__(self, text_woodruff, threshold: float, path_matches, path_matches_temporary):
        self.threshold = threshold
        self.text_woodruff = text_woodruff
        self.matches_total = pd.DataFrame()
        self.matches_current = pd.DataFrame()
        self.path_matches = path_matches
        self.path_matches_temporary = path_matches_temporary
        self.load_vectorizer()

    def load_vectorizer(self):
        self.phrases_woodruff = DataUtil.split_string_into_list(self.text_woodruff, n = 15)
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix_woodruff = self.vectorizer.fit_transform(self.phrases_woodruff)

    def run_extractor(self, data_scriptures, save=False, save_temporary=True, publish=False):
        self.progress_bar = tqdm(total=len(data_scriptures))
        for index, row in data_scriptures.iterrows():
            self.progress_bar.update(1)
            description = f"{row['verse_title']} phrase length: {len(row['scripture_text'].split())} total match count: {len(self.matches_total)}"
            self.progress_bar.set_description(description)
            # initial filter to get out very low percentage matches
            self.compute_string_match_percentages(row['scripture_text'])
            # secondary filter to remove low tfidf percentage matches
            # self.matches_current = self.compute_tfidf_percentage_match(row['scripture_text'])
            # self.extract_single_phrase_matches(row['scripture_text'])
            # print(self.matches_current)
            self.matches_current['verse_title'] = row['verse_title']
            self.matches_current['volume_title'] = row['volume_title']
            self.matches_current['book_title'] = row['book_title']
            if len(self.matches_current) > 0:
                self.matches_total = pd.concat([self.matches_total, self.matches_current]).sort_values(
                    by='percentage_match', ascending=False)[['verse_title', 'percentage_match', 'phrase_woodruff','phrase_scripture', 'volume_title']]

                if save_temporary:
                    self.matches_total.to_csv(self.path_matches_temporary, index=False)

        self.progress_bar.close()

        if save:
            self.matches_total.to_csv(self.path_matches, index=False)
            print(self.matches_total)

        if publish:
            self.quarto_publish()

    def compute_string_match_percentages(self, phrase_scripture):
        words_woodruff = self.text_woodruff.split()
        words_scripture = phrase_scripture.split()
        percentage_match_list = []
        window_list = []
        phrase_scripture_list = []
        # iterate through each n word window the same length as the verse
        for i in range(len(words_woodruff)):
            min = i
            max = i + len(words_scripture)
            if max > len(words_woodruff):
                break
            window_woodruff = " ".join(words_woodruff[min:max])
            # print('comparing...')
            # print(window)
            # print(string2)
            percentage_match_raw = DataUtil.string_percentage_match(window_woodruff, phrase_scripture)
            # raw percentage match filter
            if percentage_match_raw > .2:

                percentage_match_idfidf = self.compute_tfidf_percentage_match(window_woodruff, phrase_scripture)
                # tfidf percentage match filter
                if percentage_match_idfidf > self.threshold:
                    percentage_match_list.append(percentage_match_idfidf)
                    window_list.append(window_woodruff)
                    phrase_scripture_list.append(phrase_scripture)
        matches = pd.DataFrame({
            'phrase_woodruff' : window_list,
            'phrase_scripture' : phrase_scripture_list,
            'percentage_match' : percentage_match_list,
            })
        self.matches_current = matches.sort_values(by = 'percentage_match', ascending=False)

    def compute_tfidf_percentage_match(self, phrase_woodruff, phrase_scripture):
            # self.matches_current = pd.concat([matches, scores], axis=1).query('similarity_score > @self.threshold')
            tfidf_matrix_woodruff = self.vectorizer.transform([phrase_woodruff])
            tfidf_matrix_scriptures = self.vectorizer.transform([phrase_scripture])
            cosine_score = cosine_similarity(tfidf_matrix_woodruff, tfidf_matrix_scriptures)
            return round(cosine_score[0][0], 4)
            # scores = pd.DataFrame(scores, columns=['similarity_score'])
            # print('SCORES')
            # print(cosine_score[0])
            # matches = pd.DataFrame({
            #     'phrase_woodruff':window_woodruff,
            #     'phrase_scripture':phrase_scripture
            #     }, index = [0])

            # print(matches)
            # print('matches:')
            # print(self.matches_current)

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



