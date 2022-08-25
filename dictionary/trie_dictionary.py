from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        # frequency of the word if this letter is the end of a word
        self.frequency = frequency
        self.is_last = is_last          # True if this letter is the end of a word
        # a hashtable containing children nodes, key = letter, value = child node
        self.children: dict[str, TrieNode] = {}


class TrieDictionary(BaseDictionary):

    def __init__(self):
        self.root = TrieNode()
        pass

    def linkNode(self, word, freq):
        node = self.root
        for char in word:
            if(char in node.children):
                node = node.children[char]
            else:
                newNode = TrieNode(char)
                # dictionary = {char : value}
                node.children[char] = newNode
                node = newNode
        node.is_last = True
        node.frequency = freq

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        global trieDict
        trieDict = TrieDictionary()
        for data in words_frequencies:
            trieDict.linkNode(data.word, data.frequency)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        currentNode = trieDict.root
        for char in range(len(word)):
            for letter in currentNode.children.keys():
                if(word[char] == letter):
                    # currentNode.children[char] is a object
                    currentNode = currentNode.children[letter]
                    while(currentNode.is_last and char == len(word)-1):
                        return currentNode.frequency
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        currentNode = trieDict.root
        # word in trie: c-u-t-e (data)
        # word to add : c-u-t
        word = word_frequency.word
        for data in range(len(word)):
            for char in currentNode.children.keys():
                if(char == word[data]):
                    currentNode = currentNode.children[char]
                    while(currentNode.is_last
                          and data == len(word) - 1):
                        return False
        trieDict.linkNode(word_frequency.word, word_frequency.frequency)
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        currentNode = trieDict.root
        for char in range(len(word)):
            for letter in currentNode.children.keys():
                if(word[char] == letter):
                    preNode = currentNode
                    currentNode = currentNode.children[letter]
                    while(currentNode.is_last and char == len(word)-1):
                        if (len(currentNode.children) != 0):
                            currentNode.is_last = False
                            return True
                        else:
                            del preNode.children[letter]
                            return True
        return False

    def _dfs(self, node, preword, autocompletes):
        for child in node.children.values():
            autocomplete = preword + child.letter
            if (child.is_last):
                autocompletes.append(WordFrequency(
                    autocomplete, child.frequency))
            self._dfs(child, autocomplete, autocompletes)
        return autocompletes

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        finalList = []
        currentNode = trieDict.root
        for char in word:
            if char in currentNode.children:
                currentNode = currentNode.children[char]
            else:
                currentNode = None
        if(currentNode != None):
            finalList = trieDict._dfs(currentNode, word, [])
        if(trieDict.search(word) != 0):
            object = WordFrequency(word, currentNode.frequency)
            finalList.append(object)
        finalList.sort(key=lambda x: x.word)
        finalList.sort(reverse=True, key=lambda x: x.frequency)
        del finalList[3:]
        return finalList
