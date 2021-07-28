"""
This script returns the frequency of each word inside of a text file.

Input: text file
Output: returns list in console

Possible improvements:
- workaround weird symbols and capitalization?
- display results w/ matplotlib
- memory optimization
- unittesting not for parameters but for results

"""
from collections import defaultdict
from pprint import pprint

# reads in txt file + converts to list of strings
def read_txt_file(file):
    with open(file, errors="ignore") as f:
        content = f.read().split()
    return lowercase(content)

# goes through the list and makes everything lowercase
def lowercase(words):
    new=[]
    for word in words:
        new.append(word.lower())
    return new

# counts string freq w/ hash table
def count_freq(words):
    d=defaultdict(int)
    for x in words:
        d[x]+=1
    return d

# counts string freq w/ hash table
def count_freq(words, d):
    for x in words:
        d[x]+=1
    return d

# class Frequency_Counter(object):
#     def __init__(self, dict):
#         self.create = dict
#     def count_word(self, word):
#

if __name__ == "__main__":
    file_name = 'test_txts/million_word_corpus.txt'
    words = read_txt_file(file_name)


    # d=defaultdict(int)
    # counter = ...
    #
    # d=count_freq(counter, d)


    dictionary = count_freq(words)
    sorted_dictionary = sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)
    pprint(sorted_dictionary)
