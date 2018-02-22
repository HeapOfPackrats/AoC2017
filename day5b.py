#http://adventofcode.com/2017/day/5

import sys

def main(argv):
    #get input, otherwise prompt for input
    if len(argv) == 2:
        inputFile = open(argv[1])
    else:
        print("Please specify a file (day5b.py [filepath])")
        return

    #see url at top for specifications
    jumpList = list(map(int, inputFile.read().split()))
    jumpCount = 0
    index = 0
    offset = 0
    inputFile.close()

    while index <= (len(jumpList) - 1):
        offset = jumpList[index]
        if offset >= 3:
            jumpList[index] -= 1
        else:
            jumpList[index] += 1
        index += offset
        jumpCount += 1

    inputFile.close()
    print("It took {} steps to reach the exit".format(jumpCount))

if __name__ == "__main__":
    main(sys.argv)