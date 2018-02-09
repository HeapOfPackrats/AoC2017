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
    while True:
        prevSquares = (i-1)*8
        currSquares = i*8 

        for j in range(squaresCount - 1): 
            #first square
            if j == 0:
                value = (prev[-1] + prev[0])
            #penultimate square
            elif j == (squaresCount - 2):
                value = (curr[-1] + prev[-1] + prev[-2] + prev[0])
            #last square
            elif j == (squaresCount - 1):
                value = (curr[-1] + curr[0] + prev[-1])
            #before corners
            elif j == (squaresCount*0.75 - 1):
                value = (curr[-1] + prev[prevSquares*0.75 - 1] + prev[prevSquares*.75 - 2])
            elif j == (squaresCount*0.50 - 1):
                value = (curr[-1] + prev[prevSquares*0.50 - 1] + prev[prevSquares*.50 - 2])
            elif j == (squaresCount*0.25 - 1): 
                value = (curr[-1] + prev[prevSquares*0.25 - 1] + prev[prevSquares*.25 - 2])
            #corners
            elif j == (squaresCount*0.75 - 1):
                value = (curr[-1] + prev[prevSquares*0.75 - 1])
            elif j == (squaresCount*0.50 - 1):
                value = (curr[-1] + prev[prevSquares*0.50 - 1])
            elif j == (squaresCount*0.25 - 1): 
                value = (curr[-1] + prev[prevSquares*0.25 - 1])
            #after corners
            elif j == (squaresCount*0.75):
                value = (curr[-1] + curr[-2] + prev[prevSquares*0.75 - 1])
            elif j == (squaresCount*0.50):
                value = (curr[-1] + curr[-2] + prev[prevSquares*0.50 - 1])
            elif j == (squaresCount*0.25): 
                value = (curr[-1] + curr[-2] + prev[prevSquares*0.25 - 1])

if __name__ == "__main__":
    main(sys.argv)