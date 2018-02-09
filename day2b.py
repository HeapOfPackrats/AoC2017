#http://adventofcode.com/2017/day/2

import sys

def main(argv):
    #get input, otherwise prompt for input
    if len(argv) == 2:
        inputFile = open(argv[1])
    else:
        print("Please specify a file (day2.py [filepath])")
        return

    #for each line of input, find two int such that they produce a whole quotient
    #then add said quotient to running total
    sum = 0
    for line in inputFile:
        nums = [int(n) for n in line.split()]

        for p in nums:
            for q in nums:
                if p <= q:
                    continue
                elif p%q == 0:
                    sum += p/q
    
    inputFile.close()
    print(sum)

if __name__ == "__main__":
    main(sys.argv)