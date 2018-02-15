#http://adventofcode.com/2017/day/4

import sys

def main(argv):
    #get input, otherwise prompt for input
    if len(argv) == 2:
        inputFile = open(argv[1])
    else:
        print("Please specify a file (day4.py [filepath])")
        return

    #for each line of inputFile, check if all words are unique
    #ennumerate lines with all unique words

    uniqueLineCount = 0 
    for line in inputFile:
        wordList = line.split()
        uniqueLine = True
        for word in wordList:
            if wordList.count(word) > 1:
                uniqueLine = False
                break
            else:
                continue
        if uniqueLine == True:
            uniqueLineCount += 1
    
    inputFile.close()
    print("There are {} valid passphrases".format(uniqueLineCount))

if __name__ == "__main__":
    main(sys.argv)