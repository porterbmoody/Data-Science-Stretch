

# Woodruff Match Extractor Docs..

- [run_match_extractor.py](run_match_extractor.py) python script that cleans the data and runs the MatchExtractor class comparing the scripture dataset phrases with the woodruff journal entries dataset.

- [MatchExtractor.py](MatchExtractor.py) class that takes in Woodruff journal entries dataset, splits the entries into a list of `phrase_length` word phrases, then

- [StringUtil.py](StringUtil.py) String and pandas dataframe utility class to fix some the garbage existing pandas dataframe methods. Let's be honest, pandas has some room to improve.