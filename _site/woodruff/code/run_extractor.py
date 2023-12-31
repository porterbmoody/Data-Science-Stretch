#%%
import pandas as pd
from StringUtil import StringUtil
from MatchExtractor import MatchExtractor
import warnings

pd.set_option('display.max_colwidth', None)
# warnings.filterwarnings('ignore')

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
    # r'\.|\:|\;|\,|\(|\)|\?' : r'',
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

#%%
path_root = '../data/matches/all_books_10_words/'
path_data_woodruff_raw   = '../data/raw/data_woodruff_raw.csv'
path_data_woodruff_raw   = '../data/raw/derived_data.csv'
# path_data_woodruff_clean = path_root + 'data_woodruff_clean.csv'
path_data_scriptures     = '../data/raw/data_scriptures.csv'
path_matches = '../data/matches/data_matches2.csv'

# url paths
url_woodruff = "https://github.com/wilfordwoodruff/Main-Data/raw/main/data/derived/derived_data.csv"
url_scriptures = 'https://github.com/wilfordwoodruff/wilford_woodruff_hack23/raw/main/data/lds-scriptures.csv'

# load data
data_scriptures = pd.read_csv(path_data_scriptures)
data_woodruff = pd.read_csv(path_data_woodruff_raw)

# clean woodruff data
columns = ['Internal ID', 'Parent ID', 'Order', 'Document Type', 'Website URL', 'Dates', 'Text Only Transcript']
new_columns = {'Internal ID':'internal_id',
               'Parent ID':'parent_id',
               'Order':'order',
               'Document Type':'document_type',
               'Website URL':'website_url',
               'Dates':'dates',
               'Text Only Transcript':'text_woodruff'
               }
data_woodruff = data_woodruff.rename(columns=new_columns)[list(new_columns.values())]
data_woodruff = data_woodruff.query("document_type=='Journals'")
# text = StringUtil.combine_rows(data_woodruff['text'])
data_woodruff['text_woodruff'] = StringUtil.str_replace_column(data_woodruff['text_woodruff'], replacements_woodruff)
# data_woodruff.info()
data_woodruff

#%%
# clean scripture data
data_scriptures = data_scriptures.rename(columns={'text':'text_scriptures'})
# data_scriptures['text_scriptures'] = StringUtil.str_replace_column(data_scriptures['text_scriptures'], scripture_replacements)

# filter to certain volumes
volume_titles = [
     'Old Testament',
     'New Testament',
     'Book of Mormon',
     'Doctrine and Covenants',
     'Pearl of Great Price',
     ]
data_scriptures = data_scriptures.query("volume_title in @volume_titles")
# query = "verse_title == 'Doctrine and Covenants 136:11'|verse_title == 'Doctrine and Covenants 136:12'|verse_title == 'Doctrine and Covenants 136:13'|verse_title == 'Doctrine and Covenants 136:14'|verse_title == 'Doctrine and Covenants 136:15'|verse_title == 'Doctrine and Covenants 136:16'|verse_title == 'Doctrine and Covenants 136:17'"
# data_scriptures = data_scriptures.query(query)
data_scriptures

#%%

phrase_length = 10
threshold = .7
print('volumes:', volume_titles)
print('phrase length:', phrase_length)
print('threshold:', threshold)
match_extractor = MatchExtractor(data_woodruff.copy(),
                                 data_scriptures.copy(),
                                 phrase_length,
                                 threshold=threshold)
# iterate through each row of scripture phrases dataset and run TFIDF model and cosine similarity.
match_extractor.run_extractor(path_matches=path_matches, git_push = True, quarto_publish=False)

match_extractor.matches_total


#%%

import pandas as pd
path = '../data/matches/data_matches2.csv'

data = pd.read_csv(path).sort_values(by = 'cosine_score', ascending=False)


data.sample(5)


#%%
