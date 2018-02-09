#http://adventofcode.com/2017/day/1

import sys

def main(argv):
    #get input, otherwise prompt for input
    if (len(argv) == 2):
        inputStr = argv[1]
        sum = 0
    else:
        print("Please specify an input argument (day1b.py [input])")
        return

    #find any char whose int value is equal to the char at the index length/2 ahead of it
    #add those specific chars' int values to sum
    inputLen = len(inputStr)
    offset = int(inputLen/2)
    for index, char in enumerate(inputStr):
        nextChar = inputStr[(index+offset)%(inputLen)]
        if char == nextChar:
            sum += int(char)

    print(sum)

if __name__ == "__main__":
    main(sys.argv)