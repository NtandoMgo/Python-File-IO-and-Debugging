#
# MNGNTA011
# 15 June 2021

from searchanagrams import *

def le(length,array):
    ar = []
    for word in array:
        if len(word)==length:
            ar.append(word)

    return ar

def main():
    print("***** Anagram Set Search *****")
    length = int(input("Enter word length:\n"))
    print ("Searching...")
    filename = input ("Enter file name:\n")
    fil = file_read("EnglishWords.txt")

    if fil != None:
        file_words = le(length, fil)
        #print (file_words)
        print ("Writing results...")

        res = []
        for w in file_words:
            temparray = []
            # print (anagram_find (file_words, w))
            for i in range (len (file_words)):
                tempword = []
                tempword1 = []
                tempword[:0] = w.lower()
                a = file_words[i]
                tempword1 = a[:-1]
                if tempword == tempword1 and a[:-1].lower != w.lower():
                    temparray.append (file_words[i])
            res.append (temparray)
        
        print (res)

        # try:
        #     f = open(filename, 'w')
        #     for word in file_words:
        #         ar = anagram_find(file_words, word)
        #         if ar[0] != 'S':
        #             ar.append(word)
        #             ar.sort()
        #             f.writeline(ar)
                
        #             print(ar)
        #     f.close()
        # except:
        #     print("File error")
    
if __name__ == '__main__':
    main()