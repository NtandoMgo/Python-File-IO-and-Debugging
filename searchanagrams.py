#
# MNGNTA011
# 15 June 2021

from array import array


def file_read(nameoffile):
    try:
        f = open(nameoffile,'r')
        fr = f.readlines()
        f.close()
        return fr[fr.index('START\n')+1:]
    except:
        print("Sorry, could not find file '{}'.".format(nameoffile))

def anagram_find(array, word):
    matching_words = []
    for w in array:
        b = []
        c = []
        b[:0] = word.lower()
        c[:0] = w[:-1]
        b.sort()
        c.sort()
        if b == c and (w[:-1] != word.lower()):
            matching_words.append(w[:-1])
    
    if len(matching_words) == 0:
        return "Sorry, anagrams of '"+word+"' could not be found."
    else:
        return matching_words

def main():
    print('***** Anagram Finder *****')
    array = file_read('EnglishWords.txt')

    if array != None:
        inp = input('Enter a word:\n')
        print(anagram_find(array, inp))

if __name__ == '__main__':
    main()