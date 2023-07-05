import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import numpy as np



class StringUtil:
    """ Utility class for cleaning the data
    """

    @staticmethod
    def str_split(string, remove_duplicates = True, stop_words = None):
        if type(string) == float:
            print(string)
        words = string.split(' ')
        if remove_duplicates:
            words = list(set(words))
        return words

    @staticmethod
    def combine_rows(column):
        """ pass in a column, or list of strings, and it returns a joined string separated by ' '
        """
        return ' '.join(str(cell) for cell in column)

    @staticmethod
    def regex_filter(dataframe, column, regex):
        """ Remove rows that have regex match in certain string column
        """
        return dataframe[dataframe[column].str.contains(regex) == False]

    @staticmethod
    def str_replace(string, regex, replacement):
        """ Pass in string, regex pattern, and replacement string
            it finds all occurences of regex pattern in the string and replaces them
            with replacement string
        """
        return re.sub(regex, replacement, string)

    @staticmethod
    def str_replace_column(column, replacement_dict):
        """ Inputs: a replacement dictionary, and pandas series or a single column of a pandas dataframe
            Outputs: a single pandas series
            Iterates through each element of replacement dictionary and replaces it with
        """
        for regex, replacement in replacement_dict.items():
            # output_string = re.sub(regex, replacement, output_string)
            column = column.apply(lambda x: StringUtil.str_replace(x, regex, replacement))
        return column

    @staticmethod
    def str_extract(string, regex):
        """ Returns first and only first match. If no matches, returns empty string
        """
        matches = re.findall(regex, string)
        if len(matches) > 0:
            return matches[0]
        return ''

    @staticmethod
    def str_extract_all(string, regex):
        """ Returns list of regex match patterns
        """
        return re.findall(regex, string)

    @staticmethod
    def str_count_occurrences(string, regex):
        """ Counts ocurrences of a certain keyword within string and
            returns int
        """
        return len(StringUtil.str_extract_all(string, regex))

    @staticmethod
    def remove_duplicate_words(string):
        # Split the string into individual words
        words = string.split()

        # Use a set to remove duplicates while preserving the order
        unique_words = list(set(words))

        # Join the unique words back into a string
        return ' '.join(unique_words)

    @staticmethod
    def str_remove(string, regex):
        return re.sub(regex, r'', string)

    @staticmethod
    def str_detect(string, regex):
        return bool(re.search(pattern = regex, string=string))

    @staticmethod
    def str_remove_list(string, regex_list):
        for regex in regex_list:
            string = re.sub(regex, '', string)
        return string

    @staticmethod
    def str_replace_list(string, regex_list, replacement):
        """Pass in a string, a list of regex patterns, and a single replacement string. It loops through each regex pattern and replaces it with the given replacement pattern
        """
        for regex in regex_list:
            if regex == r'\s\d+\s' and StringUtil.str_detect(string, regex):
                # print("PIZZA")
                # print(string)
                print(re.sub(regex, replacement, string))
            string = re.sub(regex, replacement, string)
        return string

    # @staticmethod
    # def remove_stop_words(string):
    #     return StringUtil.str_replace_list(string, regex_list = stop_words, replacement = ' ')

    @staticmethod
    def split_string_into_list(string, n, increment = 0):
        """ Basically converts a string of text into a list of strings of text
        each element containing n words.
        Except the last few words get attatched on the end of the last element of the list,
        but only if the number of remaining words is > n/2 or more than half of n
        """
        words = string.split()
        result = []
        for i in range(0, len(words), n):
            if i + n < len(words) + round(n/2) or len(result) == 0:
                phrase = ' '.join(words[i : i + n])
                result.append(phrase)
            else:
                phrase = ' '.join(words[i : i + n])
                result[-1] += ' ' + phrase
        return result

    @staticmethod
    def create_frequency_dist(string):
        """ Returns pandas dataframe containing frequencies of each word in string
        """
        string = string.lower()
        tokens = word_tokenize(string)
        frequency_distribution = FreqDist(tokens)
        data = pd.DataFrame(list(frequency_distribution.items()), columns=['word', 'frequency'])
        print(data.shape)
        return data.sort_values(by = 'frequency', ascending = False)

    @staticmethod
    def string_percentage_match(string1, string2):
        words1 = string1.split()
        words2 = string2.split()
        word_matches = [word1 for word1 in words1 if word1 in words2]
        return round(len(word_matches) / len(string1.split()), 4)

    @staticmethod
    def count_words(string):
        return len(StringUtil.str_split(string))

    @staticmethod
    def get_dataframe_chunks(data, chunk_size):
        """ pass in dataframe and number of rows as chunk_size
            iterates through dataframe and saves each chunk of the dataframe to a list
        """
        data_chunks = []
        for i in range(0, len(data), chunk_size):
            min = i
            max = i + chunk_size
            if max > len(data):
                max = len(data)
            data_chunk = data.iloc[min:max]
            data_chunks.append(data_chunk)

        return data_chunks
