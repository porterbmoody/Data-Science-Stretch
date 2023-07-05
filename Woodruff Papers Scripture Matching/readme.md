

# Woodruff Match Extractor Docs..

## [quarto site](https://porter.quarto.pub/data-science-stretch/articles/wwp.html)

## code
	- [run_match_extractor.py](code/run_match_extractor.py) python script that cleans the data and runs the MatchExtractor class comparing the scripture dataset phrases with the woodruff journal entries dataset.

	- [MatchExtractor.py](code/MatchExtractor.py) class that takes in Woodruff journal entries dataset, splits the entries into a list of `phrase_length` word phrases, then

	- [StringUtil.py](code/StringUtil.py) String and pandas dataframe utility class to fix some the garbage existing pandas dataframe methods. Let's be honest, pandas has some room to improve.

## data
- [data_matches_temporary.csv](data/data_matches_temporary.csv) csv containing all the current matches found
- [data_matches.csv](data/data_matches.csv) csv containing total matches after `run_extractor` is fully run
- [data_woodruff_raw.csv](data/data_woodruff_raw.csv) csv containing original woodruff entries. separated by date i believe.
- [data_scriptures.csv](data/data_scriptures.csv) very clean csv of all verses in entries standard works including articles of faith and joseph smith history. very cool and awesome