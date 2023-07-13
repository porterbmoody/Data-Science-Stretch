


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


# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from StringUtil import StringUtil
# import numpy as np

# cool_dict1 = {
#     'text' : ['hello my name is bob fitsgerald i live in rexburg it is so great here wow ok', 'hello i like pizza hearken o ye people of my church it is very delicious']
# }
# cool_dict2 = {
#     'text' : ['hearken o ye people of my church i am god and i never make mistakes i am perfect and i know all things and nothing is hidden from mine eyes']
# }
# data1 = pd.DataFrame(cool_dict1)
# data2 = pd.DataFrame(cool_dict2)
# data1


#%%
# data.explode(column_name).reset_index(drop=True)
# phrase_length = 10
# data_expanded1 = StringUtil.expand_dataframe_of_text(data1.copy(), 'text', phrase_length)
# data_expanded2 = StringUtil.expand_dataframe_of_text(data2.copy(), 'text', phrase_length)
# data_expanded1
# data_expanded2


# vectorizer = TfidfVectorizer()
# vectorizer.fit_transform(data_expanded1['text'])

# tfidf_matrix1 = vectorizer.transform(data_expanded1['text'])
# tfidf_matrix1
# tfidf_matrix2 = vectorizer.transform(data_expanded2['text'])
# tfidf_matrix2

# similarities = cosine_similarity(tfidf_matrix1, tfidf_matrix2)
# similarities
# #%%
# data_expanded1['vector'] = similarities
# data_expanded1

# #%%
# similarities.max(axis=0)

# #%%
# # Map the scores back to the dataframes
# data_expanded1['similarity_scores'] = similarities.max(axis=1)
# data_expanded2['similarity_scores'] = similarities.max(axis=0)

# print("Dataframe 1:")
# print(data_expanded1)

# print("Dataframe 2:")
# print(data_expanded2)
############### swag awesomeness
    # def filter_to_matches_only_data(self):
    #     """ The first extraction algorithm is a much smaller runtime so it is run first.
    #         Then second algorithm is run that also finds extensions which takes longer to run.
    #         This method filters the data to only verses and entries that matches have already been found within.
    #     """
    #     # filter input data down to rows that already contain matches
    #     if not len(self.matches_total) > 0:
    #         self.matches_total =  pd.read_csv(self.path_matches_temporary)
    #     date_matches = list(self.matches_total['date'].unique())
    #     self.data_woodruff_filtered = self.data_woodruff.query('date in @date_matches')[['date','text']]

    #     verse_matches = list(self.matches_total['verse_title'].unique())
    #     self.data_scriptures_filtered = self.data_scriptures.query('verse_title in @verse_matches')


    # def extract_matches_extensions(self):
    #     """ Double for loop looping through expanded woodruff entries dataframe and expanded scriptures dataframe
    #         checks each phrase with each other phrase. If the score is above the threshold it uses a while loop to check for extensions of each phrase
    #         index values are stored in a list each time a score is calculated for each phrase
    #         that way it can detect if 2 phrases have already been compared and skip to the next phrases
    #         it appends all matche data to lists and creates a pandas dataframe with each list as a column to be saved to a csv
    #     """
    #     matches_woodruff = []
    #     matches_scriptures = []
    #     scores = []
    #     total_match_indices = []
    #     dates = []
    #     verse_titles = []
    #     volume_titles = []
    #     progress_bar = tqdm(total=len(list(self.data_woodruff_filtered['text'])) - 1)
    #     extension_count = 0
    #     for index1, text_woodruff in enumerate(list(self.data_woodruff_filtered['text'])):
    #         progress_bar.update(1)
    #         current_date = self.data_woodruff_filtered.iloc[index1]['date']
    #         progress_bar.set_description('current_date:'+str(current_date)+'extensions found: ' + str(extension_count))
    #         for index2, text_scriptures in enumerate(list(self.data_scriptures_filtered['text'])):
    #             current_match_indices = []
    #             if (index1, index2) in list(itertools.chain.from_iterable(total_match_indices)):
    #                 # print('repeat:', (index1, index2))
    #                 continue
    #             current_match_indices.append((index1, index2))
    #             text_woodruff_copy = text_woodruff
    #             text_scriptures_copy = text_scriptures
    #             score = StringUtil.compute_similarity(self.vectorizer, text_woodruff_copy, text_scriptures_copy)
    #             if score > self.threshold:
    #                 current_verse_title = self.data_scriptures_filtered.iloc[index2]['verse_title']
    #                 current_volume_title = self.data_scriptures_filtered.iloc[index2]['volume_title']
    #                 index1_extension = index1
    #                 index2_extension = index2
    #                 while True:
    #                     index1_extension += 1
    #                     index2_extension += 1
    #                     if index1_extension > len(list(self.data_woodruff_filtered['text']))-1:
    #                         break
    #                     if index2_extension > len(list(self.data_scriptures_filtered['text']))-1:
    #                         break
    #                     text_woodruff_extension = list(self.data_woodruff_filtered['text'])[index1_extension]
    #                     text_scriptures_extension = list(self.data_scriptures_filtered['text'])[index2_extension]
    #                     score_extension = StringUtil.compute_similarity(self.vectorizer, text_woodruff_extension, text_scriptures_extension)
    #                     if score_extension > self.threshold:
    #                         extension_count += 1
    #                         current_match_indices.append((index1_extension, index2_extension))
    #                         # print('adding extensions...', (index1_extension, index2_extension))
    #                         text_woodruff_copy += ' ' + text_woodruff_extension
    #                         text_scriptures_copy += ' ' + text_scriptures_extension
    #                     else:
    #                         break
    #                 # compute new score with extensions included
    #                 score = StringUtil.compute_similarity(self.vectorizer, text_woodruff_copy, text_scriptures_copy)
    #                 total_match_indices.append(current_match_indices)
    #                 matches_woodruff.append(text_woodruff_copy)
    #                 matches_scriptures.append(text_scriptures_copy)
    #                 dates.append(current_date)
    #                 verse_titles.append(current_verse_title)
    #                 volume_titles.append(current_volume_title)
    #                 scores.append(score)
    #                 matches_dict = {
    #                     'date' : dates,
    #                     'verse_title' : verse_titles,
    #                     'volume_title' : volume_titles,
    #                     'phrase_indices' : total_match_indices,
    #                     'score' : scores,
    #                     'matches_woodruff' : matches_woodruff,
    #                     'matches_scriptures' : matches_scriptures,
    #                 }
    #                 self.matches_extensions = pd.DataFrame(matches_dict).sort_values(by = 'score', ascending=False)
    #                 self.matches_extensions.to_csv(self.path_matches_extensions_temporary, index = False)
    #     progress_bar.close()
