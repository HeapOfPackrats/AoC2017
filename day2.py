#http://adventofcode.com/2017/day/2

import sys

def main(argv):
    #get input, otherwise prompt for input
    if len(argv) == 2:
        inputFile = open(argv[1])
    else:
        print("Please specify a file (day2.py [filepath])")
        return

    #for each line of input, find difference between largest and smallest values
    #then add difference between largest and smallest to running total
    sum = 0
    for line in inputFile:
        nums = [int(n) for n in line.split()]
        #saving the tiniest bit of memory here
        smallest = largest = nums[0]

        for num in nums:
            if num < smallest:
                smallest = num
            elif num > largest:
                largest = num
            else:
                continue

        sum += (largest - smallest)
    
    inputFile.close()
    print(sum)

if __name__ == "__main__":
    main(sys.argv)