import os
from WordTracker import *
from WordExtractor import *
class PathIterator(object):
    """
    An iterator which iterates over all the directories and files
    in a given path (note - in the path only, not in the
    full depth). There is no importance to the order of iteration.
    """
    def __init__(self,path):

        self.files_list = os.listdir(path)
        self.pointer = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer == len(self.files_list):
            raise StopIteration
        return_file = self.files_list[self.pointer]
        self.pointer += 1
        return return_file


def path_iterator(path):
    """
    Returns an iterator to the current path's filed and directories.
    Note - the iterator class is not outlined in the original
     version of this file - but rather is should be designed
     and implemented by you.
    :param path: A (relative or an absolute) path to a directory.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :return: An iterator which returns all the files and directories
    in the *current* path (but not in the *full depth* of the path).
    """

    return PathIterator(path)



def print_tree(path, sep='  '):
    """
    Print the full hierarchical tree of the given path.
    Recursively print the full depth of the given path such that
    only the files and directory names should be printed (and not
    their full path), each in its own line preceded by a number
    of separators (indicated by the sep parameter) that correlates
    to the hierarchical depth relative to the given path parameter.
    :param path: A (relative or an absolute) path to a directory.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :param sep: A string separator which indicates the depth of
     current hierarchy.
    """

    files = os.listdir(path)
    print (path)
    for i in range (1,len(files)):
        newpath = path+"/"+files[i]
        if os.path.isdir(newpath):
            print_tree(newpath,sep*2)
        print (sep+files[i])

    
def file_with_all_words(path, word_list):
    """
    Find a file in the full depth of the given path which contains
    all the words in word_list.
    Recursively go over  the files in the full depth of the given
    path. For each, check whether it contains all the words in
     word_list and if so return it.
    :param path: A (relative or an absolute) path to a directory.
    In the full path of this directory the search should take place.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :param word_list: A list of words (of strings). The search is for
    a file which contains this list of words.
    :return: The path to a single file which contains all the
    words in word_list if such exists, and None otherwise.
    If there exists more than one file which contains all the
    words in word_list in the full depth of the given path, just one
    of theses should be returned (does not matter which).
    """
    my_dictionary = WordTracker(word_list)
    dictionary = my_dictionary.sorted_dictionary
    for i in PathIterator(path):
        newpath = path + "/" + i
        if os.path.isdir(newpath):
            file_with_all_words (newpath, word_list)
        elif os.path.isfile(newpath):
            for word in WordExtractor(newpath):
                for dictionary_word in dictionary:
                    if word == dictionary_word:
                        my_dictionary.encounter(word)
                    if my_dictionary.encountered_all():
                        return newpath

x = file_with_all_words("ex5",["this","is","test"])
print (x)
    

