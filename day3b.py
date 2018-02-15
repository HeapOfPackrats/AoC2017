#http://adventofcode.com/2017/day/3

import sys

def main(argv):
    #get input, otherwise prompt for input
    if (len(argv) == 2):
        inputSquare = int(argv[1])
    else:
       print("Please specify an input argument (day3.py [input])")
       return

    #find first square that contains a value larger than input

    #hard-coded logic for first two boxes of squares (#0, #1 zero-indexed)
    for value in [1, 2, 4, 5, 10, 11, 23, 25]:
        if value > inputSquare:
            print("{} is the first value larger than the input.".format(value))

    #iterate through boxes from the third (box #2) onward until answer is found
    prev = [1, 2, 4, 5, 10, 11, 23, 25]
    curr = []
    i = 2
    while i > 0:
        prevSquares = (i-1)*8
        prevUpperRight = int(prevSquares*0.25 - 1)
        prevUpperLeft = int(prevSquares*0.50 - 1)
        prevLowerLeft = int(prevSquares*0.75 - 1)

        currSquares = i*8
        currUpperRight = int(currSquares*0.25 - 1)
        currUpperLeft = int(currSquares*0.50 - 1)
        currLowerLeft = int(currSquares*0.75 - 1)
        
        for j in range(currSquares):
            #sides
            if 1 <= j < (currUpperRight - 1):
                value = (curr[-1] + prev[j] + prev[j-1] + prev[j-2])
            elif (currUpperRight + 1) < j < (currUpperLeft - 1):
                value = (curr[-1] + prev[j-2] + prev[j-3] + prev[j-4])
            elif (currUpperLeft + 1) < j < (currLowerLeft - 1):
                value = (curr[-1] + prev[j-4] + prev[j-5] + prev[j-6])
            elif (currLowerLeft + 1) < j < (currSquares - 2):
                value = (curr[-1] + prev[j-6] + prev[j-7] + prev[j-8])
            #pre-corner
            elif j == (currUpperRight - 1): 
                value = (curr[-1] + prev[prevUpperRight] + prev[prevUpperRight - 1])
            elif j == (currUpperLeft - 1):
                value = (curr[-1] + prev[prevUpperLeft] + prev[prevUpperLeft - 1])
            elif j == (currLowerLeft - 1):
                value = (curr[-1] + prev[prevLowerLeft] + prev[prevLowerLeft - 1])
            #corners
            elif j == (currUpperRight): 
                value = (curr[-1] + prev[prevUpperRight])
            elif j == (currUpperLeft):
                value = (curr[-1] + prev[prevUpperLeft])
            elif j == (currLowerLeft):
                value = (curr[-1] + prev[prevLowerLeft])
            #after corners
            elif j == (currUpperRight + 1): 
                value = (curr[-1] + curr[-2] + prev[prevUpperRight] + prev[prevUpperRight + 1])
            elif j == (currUpperLeft + 1):
                value = (curr[-1] + curr[-2] + prev[prevUpperLeft] + prev[prevUpperLeft + 1])
            elif j == (currLowerLeft + 1):
                value = (curr[-1] + curr[-2] + prev[prevLowerLeft] + prev[prevLowerLeft + 1])
            #first square
            elif j == 0:
                value = (prev[-1] + prev[0])
            #penultimate square
            elif j == (currSquares - 2):
                value = (curr[-1] + curr[0] + prev[-1] + prev[-2])
            #last square
            elif j == (currSquares - 1):
                value = (curr[-1] + curr[0] + prev[-1])

            if value > inputSquare:
                #print answer, kill all loops
                print("{} is the next biggest value after {}".format(value, inputSquare))
                i = 0
                break
            else:
                print(value)
                print(" ")
                curr.append(value)

        i+=1
        prev.clear()
        prev = curr
        curr = []

if __name__ == "__main__":
    main(sys.argv)