



# %%
from nltk.tokenize import word_tokenize
from StringUtil import StringUtil
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

pd.set_option('display.max_colwidth', None)



#%%


# text1 = 'hello this is a string of mostly useless text hearken o ye people of my church  saith the voice of him who dwells on high, but some super awesome cool references every now and then ok this is so awesome and cool pizza taco For verily the voice of the Lord is unto all men, and there is none to escape; and there is no eye that shall not see, neither ear that shall not hear, neither heart that shall not be penetrated'
# text2 = 'Hearken, O ye people of my church, saith the voice of him who dwells on high, and whose eyes are upon all men For verily the voice of the Lord is unto all men, and there is none to escape; and there is no eye that shall not see, neither ear that shall not hear, neither heart that shall not be penetrated'
text1 = 'hello this is a string of mostly useless text hearken o ye people of my church  saith the voice of him who dwells on high, but some super awesome cool references every now and then ok this is so awesome and cool pizza taco '
text2 = 'Hearken, O ye people of my church, saith the voice of him who dwells on high but some super awesome cool references every now and then ok'
# text1 = StringUtil.combine_rows(data_woodruff.head(1)['text'])
# text2 = StringUtil.combine_rows(data_scriptures.head(10)['text'])
text1_list = StringUtil.split_string_into_list(text1, 10)
text2_list = StringUtil.split_string_into_list(text2, 10)

vectorizer = TfidfVectorizer()
vectorizer.fit_transform(text1_list)


StringUtil.extract_matches_extensions(vectorizer, text1_list, text2_list, threshold=.4)





# %%


