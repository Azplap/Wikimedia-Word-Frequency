"""
This script returns the frequency of each word inside of a text file.

Input: text file
Output: returns list in console

"""
from collections import defaultdict

# reads in txt file + converts to list of strings
def read_txt_file(file):
    with open(file, errors="ignore") as f:
        content = f.read().split()
    return content

# counts string freq w/ hash table
def count_freq(words):
    d=defaultdict(int)
    for x in words:
        d[x]+=1
    return d


if __name__ == "__main__":
    file_name = 'description.txt'
    words = read_txt_file(file_name)
    dictionary = count_freq(words)
    sorted_dictionary = sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)
    print(sorted_dictionary)
