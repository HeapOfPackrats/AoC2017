#http://adventofcode.com/2017/day/17
#we begin with a circular buffer of length 1 containing a 0 (zero).
#a "spinlock algorithm" steps though the buffer a number of times
#that's specified by the puzzle input, then inserts/appends the value 1.
#the buffer is now of length 2 and contains 0 and 1, and the spinlock's next
#cycle starts from the index of the new element 1 (index = 1).
#this continues until the value 2017 is inserted (buffer is now 2018 long)
#we wish to know what value is at the index one ahead of the value 2017

from collections import deque

def main():
    with open("input17.txt") as inputFile:
        steps = int(inputFile.read())
    circBuffer = spinlock(steps,2017)
    print("The value after 2017 is {}".format(circBuffer[0]))

def spinlock(steps, finalVal):
    circBuffer = deque([0])
    for i in range(1,finalVal+1):
        circBuffer.rotate(-(steps%len(circBuffer)))
        circBuffer.append(i)
    return circBuffer

if __name__ == "__main__":
    main()