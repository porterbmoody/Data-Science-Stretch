#%%
import pandas as pd
from termcolor import colored
from DataUtil import DataUtil
# import cupy as cp
# from cupy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
from numba import jit, float64, typeof
import os
import numpy as np
pd.set_option('display.max_colwidth', None)

woodruff_typos = {
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
    }

woodruff_character_replacements = {
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
}

exact_replacements = {r'a b c d e f g h i j k l m n o p q r s t u v w x y z and 1 2 3 4 5 6 7 8 9 0' : r''}

scripture_replacements = {
    r'\.|\:|\;|\,|\-|\(|\)|\?' : r'',
}

#%%
os.chdir('C:/Users/porte/Desktop/coding/Data-Science-Stretch')
# local data
path_data_woodruff_raw = 'Woodruff Papers Scripture Matching/data/raw/data_woodruff_raw.csv'
path_data_woodruff_clean = 'Woodruff Papers Scripture Matching/data/raw/data_woodruff_clean.csv'
path_data_scriptures = 'Woodruff Papers Scripture Matching/data/raw/data_scriptures.csv'
path_matches = 'Woodruff Papers Scripture Matching/data/matches/top_matches.csv'

# url data
url_woodruff = "https://github.com/wilfordwoodruff/Main-Data/raw/main/data/derived/derived_data.csv"
url_scriptures = 'https://github.com/wilfordwoodruff/wilford_woodruff_hack23/raw/main/data/lds-scriptures.csv'

# load data
data_woodruff = pd.read_csv(path_data_woodruff_raw)
data_woodruff
# lowercase all text
data_woodruff['text'] = data_woodruff['text'].str.lower()

# clean woodruff data
data_woodruff['text'] = data_woodruff['text'].replace(woodruff_character_replacements, regex=True)
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

# output this just to check if cleaned data is really clean
data_woodruff.to_csv(path_data_woodruff_clean, index = False)
data_woodruff
# string = str(data_woodruff.iloc[8390][2])
# string[-175:]

#%%
text_woodruff = DataUtil.combine_rows(data_woodruff['text'])
phrases_woodruff = DataUtil.split_string_into_list(text_woodruff, n = 15)
print('woodruff phrase count:', len(phrases_woodruff))

phrases_woodruff



#%%
class MatchExtractor:

    def __init__(self, phrases_woodruff, threshold) -> None:
        self.threshold = threshold
        self.phrases_woodruff = phrases_woodruff
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix_1 = self.vectorizer.fit_transform(phrases_woodruff)

    def extract_matches_phrase(self, scripture_phrase):
        """ pass in list with single string scripture phrase and it
            returns matches dataframe
        """
        tfidf_matrix_2 = self.vectorizer.transform(scripture_phrase)

        # returns a matrix of similarity scores
        scores = cosine_similarity(self.tfidf_matrix_1, tfidf_matrix_2)
        # merge scores in with their respective phrases
        scores = pd.DataFrame(scores, columns = ['similarity_score'])

        matches = pd.DataFrame({'phrase_woodruff' : self.phrases_woodruff,
                                'phrase_scripture' : scripture_phrase[0]})

        top_matches_scores = pd.concat([matches, scores], axis=1).query('similarity_score > @self.threshold')
        return top_matches_scores.sort_values(by = 'similarity_score', ascending=False)


# data_scriptures1 = data_scriptures.iloc[:100]
data_scriptures1 = data_scriptures
data_scriptures1
#%%

progress_bar = tqdm(total=len(data_scriptures1))
total_matches = pd.DataFrame()
match_extractor = MatchExtractor(phrases_woodruff, threshold = .65)

# iterate through each row of scripture phrases dataset and run TFIDF model and cosine similarity.
for i in range(len(data_scriptures1)):
    row = list(data_scriptures1.iloc[i])
    volume_title = row[0]
    book_title = row[1]
    verse_title = row[2]
    phrases_scriptures = [row[3]]
    top_matches = match_extractor.extract_matches_phrase(phrases_scriptures)

    top_matches['verse_title'] = verse_title
    top_matches['volume_title'] = volume_title
    total_matches = pd.concat([total_matches, top_matches]).sort_values(by = 'similarity_score', ascending=False)
    total_matches.to_csv(path_matches, index = False)

    progress_bar.update(1)
    description = verse_title + ' total match count: ' + str(len(total_matches))# + 'verse length: ' + str(len(phrases_scriptures[0]))
    progress_bar.set_description(description)

progress_bar.close()
total_matches

