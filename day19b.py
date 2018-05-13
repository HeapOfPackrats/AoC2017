#http://adventofcode.com/2017/day/19
#we will follow a path from the top to the exit and collect letters
#the path (our puzzle prompt), resembles this smaller example:
#      |          
#      |  +--+    
#      A  |  C    
#  F---|----E|--+ 
#      |  |  |  D 
#      +B-+  +--+
#we wish to report which letters we see (in order of encounter) after
#exiting the path

#for part 2, we wish to track how many steps we've taken

def main():
    with open("input19.txt") as inputFile:
        path = getPathFromInput(inputFile)
    letters, stepsCount = followPath(path)
    print("After following the path, we got the letters {}".format(letters))
    print("It took {} steps to follow the path".format(stepsCount))

#read the text input into a list of str that will provide easy
#row (list index) and column (str index) navigation
#(0, 0) is upper left, positive increments move down and right, respectively
def getPathFromInput(inputFile):
    path = list()
    for line in inputFile:
        path.append(line)
    return path

#follow the path, return list of letters (in order of encounter) as a str
def followPath(path):
    #on the top of path (path[0]) find the column where path starts
    for j in range(len(path[0])):
        if path[0][j] == "|":
            #begin by following path downward from starting coordinates
            currLine = "|"
            currI, currJ = 0, j
            currDirection = "down"
            letters = ""
            stepsCount = 0
    #follow path from start. " " marks the end of the path
    while currLine != " ":
        #count each step we've previously taken (including entering start)
        stepsCount += 1
        #step according to current direction
        if currDirection == "down":
            currI += 1
            currJ += 0
        elif currDirection == "right":
            currI += 0
            currJ += 1
        elif currDirection == "up":
            currI += -1
            currJ += 0
        elif currDirection == "left":
            currI += 0
            currJ += -1
        currLine = path[currI][currJ]
        #collect any letters we find along the way
        if currLine.isalpha():
            letters += currLine
        #at "+" intersections, find direction in which path continues
        elif currLine == "+":
            if currDirection == "down" or currDirection == "up":
                if path[currI][currJ+1] != " ":
                    currDirection = "right"
                elif path[currI][currJ-1] != " ":
                    currDirection = "left"
            elif currDirection == "right" or currDirection == "left":
                if path[currI+1][currJ] != " ":
                    currDirection = "down"
                elif path[currI-1][currJ] != " ":
                    currDirection = "up"
    return letters, stepsCount

if __name__ == "__main__":
    main()
