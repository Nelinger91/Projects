#!/usr/bin/env python3


class WordExtractor(object):
    """
    This class should be used to iterate over words contained in files.
     The class should maintain space complexity of O(1); i.e, regardless
     of the size of the iterated file, the memory requirements ofa class
     instance should be bounded by some constant.
     To comply with the space requirement, the implementation may assume
     that all words and lines in the iterated file are bounded by some
     constant, so it is allowed to read words or lines from the
     iterated file (but not all of them at once).
    """

    def __init__(self, filename):
       
        """
        Initiate a new WordExtractor instance whose *source file* is
        indicated by filename.
        :param filename: A string representing the path to the instance's
        *source file*
        """
        self.words = []
        self.filename = filename
        self.counter = 0
        self.position_in_file = 0
        if ".DS_Store" in filename:
            return
        with open(filename,'r') as f:
            f.seek(self.position_in_file)
            self.words = f.readline().split()
            self.position_in_file = f.tell()

            f.close()

        

    def __iter__(self):
        """
        Returns an iterator which iterates over the words in the
        *source file* (i.e - self)
        :return: An iterator which iterates over the words in the
        *source file*
        """
        return self


    def __next__(self):
        """
        Make a single word iteration over the source file.
        :return: A word from the file.
        """

        if self.words == []:
            raise StopIteration
        word_to_return = self.words[self.counter]
        self.counter += 1
        if len(self.words) == self.counter:
            with open(self.filename,'r') as f:
                f.seek(self.position_in_file)
                self.words = f.readline().split() 
                self.position_in_file = f.tell()
                f.close()
            self.counter = 0
        return word_to_return

                   
            

       
