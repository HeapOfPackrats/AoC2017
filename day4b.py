#http://adventofcode.com/2017/day/4

import sys

def main(argv):
    #get input, otherwise prompt for input
    if len(argv) == 2:
        inputFile = open(argv[1])
    else:
        print("Please specify a file (day4.py [filepath])")
        return

    #for each line of inputFile, check if all words are not anagrams of another word
    #ennumerate lines without duplicate anagrams

    uniqueLineCount = 0 
    for line in inputFile:
        wordList = line.split()
        uniqueLine = True
        for word1 in wordList:
            for word2 in wordList:
                if len(word1) == len(word2) and word1 is not word2:
                    sameChars = 0
                    for char in word1:
                        if char in word2:
                            sameChars += 1
                        else:
                            continue
                    if sameChars == len(word1):
                        uniqueLine = False
                        break

        if uniqueLine == True:
            uniqueLineCount += 1
    
    inputFile.close()
    print("There are {} valid passphrases".format(uniqueLineCount))

if __name__ == "__main__":
    main(sys.argv)