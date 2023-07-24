#%%
import pandas as pd

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', 30)

path = '../data/matches/data_matches.csv'
data = pd.read_csv(path).sort_values(by = 'cosine_score', ascending=False)

data

#%%


