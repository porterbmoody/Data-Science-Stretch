


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







