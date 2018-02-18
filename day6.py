#http://adventofcode.com/2017/day/6

import sys

def main(argv):
    #get input, otherwise prompt for input
    if len(argv) == 2:
        inputFile = open(argv[1])
    else:
        print("Please specify a file (day6.py [filepath])")
        return

    #see url at top for specifications
    memBanks = list(map(int, inputFile.read().split()))
    memBanksLog = list()
    cycles = 0
    repeat = False

    #continue memory allocation cycles until a repeat config occurs
    while repeat == False:
        memBanksLog.append(list(memBanks))
        memAdder(memBanks)
        cycles += 1
        for bank in memBanksLog:
            if memBanks == bank:
                repeat = True

    print("It took {} cycless to find a repeat memory configuration".format(cycles))

def memAdder(memBanks):
    maxIndex = max( range(len(memBanks)), key = lambda index : memBanks[index]) #clever soln thnx: https://stackoverflow.com/a/41840279
    maxValue = memBanks[maxIndex]
    memBanks[maxIndex] = 0

    #determine if there are any loops through entire mem bank + any remaining steps
    loops, remainder = divmod(maxValue, len(memBanks))

    #if the mem allocation loops around, += 1 to all elements in bank per loop
    if loops > 0:
        for i in memBanks:
            memBanks[i] += loops
    
    #finish distributing any other memory
    if remainder > 0:
        for i in range(1, remainder+1):
            memBanks[(maxIndex+i)%(len(memBanks))] += 1

if __name__ == "__main__":
    main(sys.argv)