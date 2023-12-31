#%%
import pandas as pd
from StringUtil import StringUtil
from MatchExtractor import MatchExtractor
pd.set_option('display.max_colwidth', None)

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
    r'confer ence'     : r'conference',
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
    r'traveling' : r'pizza',
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
    r'diestroy ' : r'destroy ',
    r'a b c d e f g h i j k l m n o p q r s t u v w x y z and 1 2 3 4 5 6 7 8 9 0' : r'',
    r' \^e\^ 4 \^p\^ 5 \^t\^ 1 \^d\^ 3 ': r'',
}

scripture_replacements = {
    r'\.|\:|\;|\,|\-|\(|\)|\?' : r'',
}

#%%
# local paths
path_data_woodruff_raw   = '../data/data_woodruff_raw.csv'
path_data_woodruff_clean = '../data/data_woodruff_clean.csv'
path_data_scriptures     = '../data/data_scriptures.csv'
path_matches             = '../data/data_matches.csv'
path_matches_temporary   = '../data/data_matches_temporary.csv'

# url paths
url_woodruff = "https://github.com/wilfordwoodruff/Main-Data/raw/main/data/derived/derived_data.csv"
url_scriptures = 'https://github.com/wilfordwoodruff/wilford_woodruff_hack23/raw/main/data/lds-scriptures.csv'

# load data
data_scriptures = pd.read_csv(path_data_scriptures)
data_woodruff = pd.read_csv(path_data_woodruff_raw)

# clean woodruff data
data_woodruff['text'] = StringUtil.str_replace_column(data_woodruff['text'], replacements_woodruff)

# clean scripture data
data_scriptures['scripture_text'] = StringUtil.str_replace_column(data_scriptures['scripture_text'], scripture_replacements)

#%%
match_extractor = MatchExtractor(data_woodruff, data_scriptures, phrase_length = 13)

# iterate through each row of scripture phrases dataset and run TFIDF model and cosine similarity.
match_extractor.run_extractor(
    path_matches,
    path_matches_temporary,
    threshold = .75,
    save=True,
    quarto_publish=True,
    )


# filter to certain volumes
# volume_titles = [
#      'Old Testament',
#      'New Testament',
#      'Book of Mormon',
#      'Doctrine and Covenants',
#      'Pearl of Great Price',
#      ]
# data_scriptures = data_scriptures.query("volume_title in @volume_titles")
# data_scriptures