#http://adventofcode.com/2017/day/13

#see URL at top for full specifications
#it's a bit long and complicated to detail here

def main():
    with open("input13.txt") as inputFile:
        wallSpecs, wallLength = buildFirewall(inputFile)
    print("The severity of the trip through the firewall is {}".format(moveAndScan(wallSpecs, wallLength)))

def buildFirewall(inputFile):
    wallSpecs = dict()
    for line in inputFile:
        wallDepth, scanRange = map(int, line.split(sep=": ")) #line format is always "[0-9]+: [2-9]\n" or "[0-9]+: [0-9]+\n"
        wallSpecs.update({wallDepth: scanRange}) #wallDepth is zero-indexed. scanRange is always >= 2
    wallLength = wallDepth + 1
    return wallSpecs, wallLength

#there's a more efficient way to check caughtness without ever moving the walls
#for any wall we enter at depth >0, we get caught if picoSec % (2*scanRange - 2) == 0
#the formula above are times when the wall we're entering has its scan at index 0
#in other words, we don't really need to store and update wall position, but it's a cute naive soln
def moveAndScan(wallSpecs, wallLength):
    scanPos = {k:0 for k in wallSpecs.keys()}
    myDepth = -1
    severity = 0
    for picoSec in range(wallLength):
        #move (we stay at height zero relative to walls)
        myDepth += 1
        #check if caught
        if myDepth in scanPos:
            if scanPos[myDepth] == 0:
                severity += myDepth*wallSpecs[myDepth] #depth*scanRange
        #move scans
        for wall in scanPos:
            if int(picoSec/(wallSpecs[wall]-1))%2 == 0: #scan index increases when time is in an even interval of (scanRange-1)
                scanPos[wall] += 1
            else:
                scanPos[wall] -= 1
    return severity

if __name__ == "__main__":
    main()