


entries_to_remove = [
    r'WW 1841-2',
    r'Front cover',F WILLFORD FOR 1839',
    r'W\. WOODRUFFs DAILY JOURNAL AND HISTORY IN 1842',
    r"WILFORD WOODRUFF's DAILY JOURNAL AND HISTORY IN 1843",
    r"WILLFORD WOODRUFF'S JOURNAL VOL\. 2\. AND A SYNOPSIS OF VOL\. 1\.",
    r"Willford Woodruff's Journal Containing an Account Of my life and travels from the time of my first connextion with the Church of Jesus Christ of Latter-day Saints",
    r'THE FIRST B
    r'THE SECOND BOOK OOOK OF WILLFORD VOL\. 2\. FOR 1838',
    r"WILLFORD\. WOORUFF's DAILY JOURNAL AND TRAVELS",
    r'Pgs 172\–288 are blank',
    ]


#%%
# #%%
# from numba import jit, cuda
# import numpy as np
# # to measure exec time
# from timeit import default_timer as timer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import pandas as pd
# from DataUtil import DataUtil

# # function optimized to run on gpu
# @jit(target_backend='cuda')
# def extract_matches(string):
# 	# for i in range(100000000):
# 		# a[i]+= 1
# 	for element in string.split():
# 		element += ' hello'
# 		print(element)

# if __name__=="__main__":

# 	start = timer()
# 	string = 'hello my name is porter'
# 	extract_matches(string)
# 	print("with GPU:", timer()-start)


# #%%
# def extract_matches(phrases_woodruff, tfidf_matrix_woodruff, vectorizer, phrases_scriptures):

#         tfidf_matrix_scriptures = vectorizer.transform(phrases_scriptures)

#         similarity_matrix = cosine_similarity(tfidf_matrix_woodruff, tfidf_matrix_scriptures)
#         # time.sleep(1)
#         threshold = 0.65  # Adjust this threshold based on your preference
#         similarity_scores = []
#         top_phrases_woodruff = []
#         top_phrases_scriptures = []

#         for i, phrase_woodruff in enumerate(phrases_woodruff):
#             for j, phrase_scriptures in enumerate(phrases_scriptures):
#                 similarity_score = similarity_matrix[i][j]
#                 # print(similarity_score)
#                 # print(phrase_scriptures)
#                 # print(phrase_woodruff)
#                 if similarity_score > threshold:
#                     top_phrases_woodruff.append(phrase_woodruff)
#                     top_phrases_scriptures.append(phrase_scriptures)
#                     similarity_scores.append(similarity_score)

#         data = pd.DataFrame({
#              'phrase_woodruff':top_phrases_woodruff,
#              'phrases_scriptures':top_phrases_scriptures,
#              'similarity_scores' : similarity_scores}).sort_values(by='similarity_scores',ascending=False)
#         return data

# #%%


# import numpy as np
# import numba
# from numba import cuda, jit
# from timeit import default_timer as timer
# # print(np.__version__)
# # print(numba.__version__)


# #%%
# # import cupy
# from sklearn.metrics.pairwise import cosine_similarity
# @jit(target_backend='cuda', nopython=False)
# def factorial(vector1, vector2):
#     return cosine_similarity(vector1, vector2)

# def factorial_poop(n):
#     n **= 20
#     return n

# start = timer()
# factorial(vector1 = [2,3], vector2 = [3,4])
# print("with GPU:", timer()-start)

# # factorial_poop(100)
# # print("without GPU:", timer()-start)
# # print('sauce')

# # %%
#%%



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




