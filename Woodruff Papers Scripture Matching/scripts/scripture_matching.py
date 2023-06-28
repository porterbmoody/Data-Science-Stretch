#%%
import pandas as pd
from termcolor import colored
from DataUtil import DataUtil
from MatchExtractor import MatchExtractor
# import cupy as cp
# from cupy.sparse import csr_matrix

from numba import jit, float64, typeof
import os
import numpy as np
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
os.chdir('C:/Users/porte/Desktop/coding/Data-Science-Stretch')
# local paths
path_data_woodruff_raw = 'Woodruff Papers Scripture Matching/data/data_woodruff_raw.csv'
path_data_woodruff_clean = 'Woodruff Papers Scripture Matching/data/data_woodruff_clean.csv'
path_data_scriptures = 'Woodruff Papers Scripture Matching/data/data_scriptures.csv'
path_matches = 'Woodruff Papers Scripture Matching/data/data_matches.csv'
path_matches_temporary = 'Woodruff Papers Scripture Matching/data/data_matches_temporary.csv'

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

total_matches = pd.DataFrame()
match_extractor = MatchExtractor(phrases_woodruff, threshold = .65, path_matches = path_matches, path_matches_temporary = path_matches_temporary)
match_extractor.run_extractor(data_scriptures, save = True, publish=True)

# iterate through each row of scripture phrases dataset and run TFIDF model and cosine similarity.
# match_extractor.total_matches


#%%
