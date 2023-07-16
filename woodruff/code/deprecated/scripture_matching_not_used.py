#%%
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from termcolor import colored
from DataUtil import DataUtil
from tqdm import tqdm
import subprocess
# import cupy as cp
# from cupy.sparse import csr_matrix
from numba import jit, float64, typeof
import os
import numpy as np
import time

pd.set_option('display.max_colwidth', None)

woodruff_typos = {
    r'(, b\.)'              : r'',
    r'\<U\+25CA\>'          : r'',
    r'\&amp;c?'             : r"and",
    r'\&apos;'              : r"'",
    r"(\^?FIGURES?\^?)"     : r'',
    r'[\{\}\~]'             : r'',
    r'\s{2}'                : r' ',
    r','                    : r'',
    r'\n'                   : r' ',
    r'\[\[(.*?)\|(.*?)\]\]' : r'\1',
    r'\-\s'                  : r'',
    r'\n'                 : r' ',
    r'\–'               : r'',
    r'\—'               : r'',
    r'\s+'                 : r' ',
    r'\.|\:|\;|\,|\-|\(|\)|\?' : r'',
    r'sacrafice'    : r'sacrifice',
    r'discours'     : r'discourse',
    r'travling'      : r'traveling',
    r'oclock'       : r'oclock',
    r'w\. woodruff' : r'wilford woodruff',
    r'any\s?whare'    : r'anywhere',
    r'some\s?whare'     : r'somewhere',
    r'whare'         : r'where',
    r'sumthing'      : r'something',
    r' els '         : r' else ',
    r' wil '         : r' will ',
    r'savio saviour' : r'saviour',
    r'arived'       : r'arrived',
    r'intirely    ' : r'entirely',
    r'phylosophers' : r'philosophers',
    r'baptised'     : r'baptized',
    r'benef\- it'   : r'benefit',
    r'preachi \-ng'      : r'preaching',
    r'oppor- tunities' : r'opportunities',
    r'vary'         : r'very',
    r'councellor'   : r'counselor',
    r'sircumstances' : r'circumstances',
    r'Preasent'    : r'present',
    r'sept\.'      : r'september',
    r'Sacramento Sacramento' : r'Sacramento',
    r'tryed'       : r'tried',
    r'fals'        : r'false',
    r'aprail'      : r'april',
    r'untill'      : r'until',
    r'sumwhat'      : r'somewhat',
    r'joseph smith jun' : r'joseph smith jr',
    r'miricle' : r'miracle',
    r'procedings' : r'proceedings',
    r'w odruff' : r'woodruff',
    r'prefered' : r'preferred',
    r'traveling' : r'pizza',
    r'esspecially' : r'especially',
    r'ownly' : r'only',
    r'th\[e\]' : r'the',
}

exact_replacements = {r'a b c d e f g h i j k l m n o p q r s t u v w x y z and 1 2 3 4 5 6 7 8 9 0' : r''}

scripture_replacements = {
    r'\.|\:|\;|\,|\-|\(|\)|\?' : r'',
}

#%%
os.chdir('C:/Users/porte/Desktop/coding/Data-Science-Stretch/Woodruff Papers Scripture Matching')
# local paths
path_data_woodruff_raw = 'data/data_woodruff_raw.csv'
path_data_woodruff_clean = 'data/data_woodruff_clean.csv'
path_data_scriptures = 'data/data_scriptures.csv'
path_matches = 'data/data_matches.csv'
path_matches_temporary = 'data/data_matches_temporary.csv'

# url paths
url_woodruff = "https://github.com/wilfordwoodruff/Main-Data/raw/main/data/derived/derived_data.csv"
url_scriptures = 'https://github.com/wilfordwoodruff/wilford_woodruff_hack23/raw/main/data/lds-scriptures.csv'

# load data
data_woodruff = pd.read_csv(path_data_woodruff_raw)
data_woodruff
# lowercase all text
data_woodruff['text'] = data_woodruff['text'].str.lower()

# clean woodruff data
data_woodruff['text'] = data_woodruff['text'].replace(woodruff_typos, regex=True)
data_woodruff['text'] = data_woodruff['text'].replace(exact_replacements, regex=True)

data_scriptures = pd.read_csv(path_data_scriptures)[['volume_title', 'book_title', 'verse_title', 'scripture_text']]
# clean scripture data
data_scriptures['scripture_text'] = data_scriptures['scripture_text'].str.lower()
data_scriptures['scripture_text'] = data_scriptures['scripture_text'].replace(scripture_replacements, regex=True)

# split each verse into a 15 word phrase then explode it all
data_scriptures['scripture_text'] = data_scriptures['scripture_text'].apply(lambda x: DataUtil.split_string_into_list(x, 15))
data_scriptures = data_scriptures.explode('scripture_text')

# filter to certain volumes
volume_titles = [
     'Old Testament',
     'New Testament',
     'Book of Mormon',
     'Doctrine and Covenants',
     'Pearl of Great Price',
     ]
data_scriptures = data_scriptures.query("volume_title in @volume_titles")

# output this just to check if cleaned data is clean
data_woodruff.to_csv(path_data_woodruff_clean, index = False)
data_woodruff

text_woodruff = DataUtil.combine_rows(data_woodruff['text'])
phrases_woodruff = DataUtil.split_string_into_list(text_woodruff, n = 15)
print('woodruff phrase count:', len(phrases_woodruff))

phrases_woodruff

#%%
# progress_bar = tqdm(total=len(data_scriptures))
# progress_bar.update(3000)


n_phrases = 200
base = 0
threshold = .65

vectorizer = TfidfVectorizer()
tfidf_matrix_woodruff = vectorizer.fit_transform(phrases_woodruff)

# split scriptures data into chunks of 200 rows
data_scriptures_chunks = []
for i in range(0, len(data_scriptures), n_phrases):
    min = i
    max = i + n_phrases
    if max > len(data_scriptures):
        max = len(data_scriptures)
    print(min, max)
    data_scriptures_chunks.append(data_scriptures[min:max])

data_scriptures_chunks

#%%
n_chunks = len(data_scriptures_chunks)
progress_bar = tqdm(total=len(data_scriptures_chunks[:n_chunks]))
data_matches_total = pd.DataFrame()

for data_scriptures in data_scriptures_chunks[:n_chunks]:

    phrases_scriptures = list(data_scriptures['scripture_text'])

    tfidf_matrix_scriptures = vectorizer.transform(phrases_scriptures)
    # get scores matrix
    scores_matrix = cosine_similarity(tfidf_matrix_woodruff, tfidf_matrix_scriptures)
    # convert scores matrix to dataframe with column headers as individual scripture phrases
    data_scores   = pd.DataFrame(scores_matrix, columns = phrases_scriptures)
    # create dataframe with woodruff phrases as single column
    data_matches  = pd.DataFrame({'phrase_woodruff': phrases_woodruff})
    data_matches  = pd.concat([data_matches, data_scores], axis=1)
    # pivot dataframe to long format with woodruff phrase column, scripture phrase column, and similarity score column
    data_matches  = pd.melt(data_matches, id_vars = 'phrase_woodruff', var_name='phrase_scripture', value_name = 'similarity_score')
    # arrange by similarity score and filter about threshold
    data_matches  = data_matches.sort_values(by='similarity_score', ascending=False).query("similarity_score > @threshold")
    # join verse title matches back into dataframe
    data_matches = data_matches.merge(data_scriptures, left_on='phrase_scripture', right_on='scripture_text', how='left')[['phrase_woodruff', 'verse_title', 'similarity_score', 'phrase_scripture', 'volume_title']]

    data_matches_total = pd.concat([data_matches_total, data_matches])

    progress_bar.update(1)
    progress_bar.set_description(desc = 'total matches: '+str(len(data_matches_total)))

    data_matches.to_csv('data/data_matches_temp.csv', index=False)
    data_matches_total.to_csv('data/data_matches_temporary.csv', index=False)


progress_bar.close()

data_matches_total


#%%

command = 'quarto publish'
subprocess.run(command, shell=True, input='y\n', encoding='utf-8')

# for i in range(0, len(data_scriptures), n_phrases):
# min = i
# max = i + n_phrases
# if max > len(data_scriptures):
    # max = len(data_scriptures)
# print(min, max)

# print(phrases_scriptures)


#%%

replacements_woodruff = {
    r'(, b\.)'              : r'',
    r'\<U\+25CA\>'          : r'',
    r'\&amp;c?'             : r"and",
    r'\&apos;'              : r"'",
    r"(\^?FIGURES?\^?)"     : r'',
    r'[\{\}\~]'             : r'',
    r'\n'                   : r' ',
    r'\[\[(.*?)\|(.*?)\]\]' : r'\1',
    r'\n'                   : r' ',
    r'\–|\-|\—|\-\s'        : r'',
    r'\s+'                  : r' ',
    r'\.|\:|\;|\,|\(|\)|\?' : r'',
    r'confer ence|Conferance'     : r'conference',
    r'appoin ted'     : r'appointed',
    r'sacrafice'           : r'sacrifice',
    r'discours'            : r'discourse',
    r'travling'            : r'traveling',
    r'oclock'              : r'oclock',
    r'w\. woodruff'        : r'wilford woodruff',
    r'any\s?whare'         : r'anywhere',
    r'some\s?whare'        : r'somewhere',
    r'whare'               : r'where',
    r'sumthing'            : r'something',
    r' els '               : r' else ',
    r' wil '               : r' will ',
    r'savio saviour'     : r'saviour',
    r'arived'            : r'arrived',
    r'intirely    '      : r'entirely',
    r'phylosophers'      : r'philosophers',
    r'baptised'           : r'baptized',
    r'benef\- it'       : r'benefit',
    r'preachi \-ng'      : r'preaching',
    r'oppor- tunities' : r'opportunities',
    r'vary'         : r'very',
    r'councellor'   : r'counselor',
    r'sircumstances' : r'circumstances',
    r'Preasent'    : r'present',
    r'sept\.'      : r'september',
    r'sacramento sacramento' : r'sacramento',
    r'tryed'       : r'tried',
    r'fals'        : r'false',
    r'aprail'      : r'april',
    r'untill'      : r'until',
    r'sumwhat'      : r'somewhat',
    r'joseph smith jun' : r'joseph smith jr',
    r'miricle' : r'miracle',
    r'procedings' : r'proceedings',
    r'w odruff' : r'woodruff',
    r'prefered' : r'preferred',
    r'esspecially' : r'especially',
    r'ownly' : r'only',
    r'th\[e\]' : r'the',
    r'judjment' : r'judgement',
    r'experiance' : r'experience',
    r'ingaged' : r'engaged',
    r'\[she\]' : r'she',
    r'fulnes ' : r'fulness ',
    r'interestin ' : r'interesting ',
    r'respetible ' : r'respectable ',
    r'attonement' : r'atonement',
    r'diestroy ' : r'destroy ',
    r'a b c d e f g h i j k l m n o p q r s t u v w x y z and 1 2 3 4 5 6 7 8 9 0' : r'',
    r' \^e\^ 4 \^p\^ 5 \^t\^ 1 \^d\^ 3 ': r'',
    r'W X Y Z and 1 2 3 4 5': r'',
}

scripture_replacements = {
    r'\.|\:|\;|\,|\-|\(|\)|\?' : r'',
}
