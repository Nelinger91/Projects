#!/usr/bin/env python3
import math

class WordTracker(object):
    """
    This class is used to track occurrences of words.
     The class uses a fixed list of words as its dictionary
     (note - 'dictionary' in this context is just a name and does
     not refer to the pythonic concept of dictionaries).
     The class maintains the occurrences of words in its
     dictionary as to be able to report if all dictionary's words
     were encountered.
    """

    def __init__(self, word_list):
        """
        Initiates a new WordTracker instance.
        :param word_list: The instance's dictionary.
        """
        self.dictionary = list(word_list)
        self.sorted_dictionary = []
        self.binary_search = int((len(self.dictionary))/2)
        self.sorted_length = len(self.dictionary)
        self.encountered = []
        self.counter = 0


        while len(self.dictionary) != 0:
            biggest = self.dictionary[0]
            biggest_index = 0
            for i in range(0,len(self.dictionary)):
                if biggest < self.dictionary[i]:
                    biggest = self.dictionary[i]
                    biggest_index = i
            self.sorted_dictionary.append(self.dictionary[i])
            self.dictionary.pop(i)


                


    def __contains__(self, word):
        """
        Check if the input word in contained within dictionary.
         For a dictionary with n entries, this method guarantees a
         worst-case running time of O(n) by implementing a
         binary-search.
        :param word: The word to be examined if contained in the
        dictionary.
        :return: True if word is contained in the dictionary,
        False otherwise.
        """
        while True:
            counter = 0 
            if (word == self.sorted_dictionary[self.binary_search]):
                return True
            elif word > self.sorted_dictionary[self.binary_search]:
                self.binary_search = math.floor(self.binary_search+self.sorted_length/2)
                counter +=1
            elif word < self.sorted_dictionary[self.binary_search]:
                self.binary_search = math.floor((self.binary_search)/2)
                counter +=1
            if counter > math.log(self.sorted_length):
                return False

        

    def encounter(self, word):

        """
        A "report" that the give word was encountered.
        The implementation changes the internal state of the object as
        to "remember" this encounter.
        :param word: The encountered word.
        :return: True if the given word is contained in the dictionary,
        False otherwise.
        """
        while True:
            if self.counter > math.log(self.sorted_length):
                return False
            if (word == self.sorted_dictionary[self.binary_search]):
                self.encountered.append(word)
                return True
            elif word > self.sorted_dictionary[self.binary_search]:
                self.binary_search = math.floor((self.binary_search+self.sorted_length)/2)
                self.counter +=1
                return (self.encounter(word))
            elif word < self.sorted_dictionary[self.binary_search]:
                self.binary_search = math.floor((self.binary_search)/2)
                self.counter +=1
                return (self.encounter(word))
            

    def encountered_all(self):
        """
        Checks whether all the words in the dictionary were
        already "encountered".
        :return: True if for each word in the dictionary,
        the encounter function was called with this word;
        False otherwise.
        """

        if len(self.encountered) == self.sorted_length:
            return True
        else:
            return False
        #words_
        #for i in range(len(self.encountered)):
         #   for j in range(len(self.sorted_dictionary)):
          #      if self.encountered[i] == self.sorted_dictionary:

        #pass

    def reset(self):
        self.encountered = []
        """
        Changes the internal representation of the instance such
        that it "forget" all past encounters. One implication of
        such forgetfulness is that for encountered_all function
        to return True, all the dictionaries' entries should be
        called with the encounter function (regardless of whether
        they were previously encountered ot not).
        """
        pass


