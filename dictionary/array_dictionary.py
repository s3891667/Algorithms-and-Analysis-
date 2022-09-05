from dictionary import word_frequency
from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt
# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


class ArrayDictionary(BaseDictionary):

    def __init__(self):
        self.words_frequencies = []
        self.time = 0
        pass

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # read the file, split it and add to the dictionary
        self.words_frequencies = words_frequencies
        self.words_frequencies.sort(key=lambda x: x.word)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        for data in self.words_frequencies:
            if (data.word == word):
                return int(data.frequency)
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        for data in self.words_frequencies:
            if(word_frequency.word == data.word):
                return False
        self.words_frequencies.append(word_frequency)
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # find the position of 'word' in the list, if exists, will be at idx-1
        for data in self.words_frequencies:
            if(data.word == word):
                self.words_frequencies.remove(data)
                return True
        return False

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        freqList = []
        for data in self.words_frequencies:
            largest = 0
            if (data.word.startswith(prefix_word) and data.frequency > largest):
                freqList.append(data)
                freqList.sort(reverse=True, key=lambda x: x.frequency)
        del freqList[3:]
        return freqList
