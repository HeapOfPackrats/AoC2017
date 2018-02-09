#http://adventofcode.com/2017/day/1

import sys

def main(argv):
    #get input, otherwise prompt for input
    if (len(argv) == 2):
        inputStr = argv[1]
        sum = 0
    else:
        print("Please provide an input argument (day1.py [input])")
        return

    #find any char that equals next Char, then adds those char's int value to sum
    inputLen = len(inputStr)
    for index, char in enumerate(inputStr):
        nextChar = inputStr[(index+1)%(inputLen)]
        if char == nextChar:
            sum += int(char)

    print(sum)

if __name__ == "__main__":
    main(sys.argv)