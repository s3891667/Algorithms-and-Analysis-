from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None


# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


class LinkedListDictionary(BaseDictionary):
    def __init__(self):
        self.head = None
        self.next = None
        pass

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        self.head = ListNode(words_frequencies[0])
        node = self.head
        for i in range(1, len(words_frequencies)):
            node.next = ListNode(words_frequencies[i])
            node = node.next

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        current = self.head
        while(current.next):
            if(current.word_frequency.word == word):
                return current.word_frequency.frequency
            current = current.next
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        current = self.head
        while(current.next):
            if(current.word_frequency.word == word_frequency.word):
                return False
            current = current.next
        insertNode = ListNode(word_frequency)
        oldNode = self.head
        self.head = insertNode
        current = self.head
        current.next = oldNode
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        if (self.head.word_frequency.word == word):
            current = self.head
            self.head = current.next
            del current
            return True
        else:
            current = self.head
            while(current.next):
                if(current.next.word_frequency.word == word):
                    delNode = current.next
                    del current.next
                    nodeAfter = delNode.next
                    current.next = nodeAfter
                    return True
                current = current.next
        return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        freqList = []
        current = self.head
        while(current.next):
            if(current.word_frequency.word.startswith(word)):
                freqList.append(current.word_frequency)
                freqList.sort(key=lambda x: x.word)
            current = current.next
        freqList.sort(reverse=True, key=lambda x: x.frequency)
        del freqList[3:]
        return freqList
