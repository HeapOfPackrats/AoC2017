#http://adventofcode.com/2017/day/17
#we begin with a circular buffer of length 1 containing a 0 (zero).
#a "spinlock algorithm" steps though the buffer a number of times
#that's specified by the puzzle input, then inserts/appends the value 1.
#the buffer is now of length 2 and contains 0 and 1, and the spinlock's next
#cycle starts from the index of the new element 1 (index = 1).
#this continues until the value 2017 is inserted (buffer is now 2018 long)
#we wish to know what value is at the index one ahead of the value 2017

#for part 2, we want to know the value one ahead of the value 0 after
#the spinlock takes 50 million values (1...50mil) into the circular buffer

from collections import deque

def main():
    with open("input17.txt") as inputFile:
        steps = int(inputFile.read())
    valAfter0 = spinlock50M(steps, 50000000)
    print("The value following 0 after fifty million spinlocks is {}".format(valAfter0))

#spinlock without a real circular buffer because we only care to track
#value 0 and whatever gets written after value 0
def spinlock50M(steps, maxVal):
    currPos = 0
    for n in range(1, maxVal+1):
        currPos = (currPos+steps)%n + 1
        if currPos == 1:
            valAfter0 = n
    return valAfter0

if __name__ == "__main__":
    main()