#http://adventofcode.com/2017/day/13

#see URL at top for full specifications
#it's a bit long and complicated to detail here
#for part 2 of day 13, check find the start time results in a severity of 0 (as detailed at URL)

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
#for any wall we enter at depth >0, we get caught if (picoSec % (2*scanRange - 2) == 0
#the formula above are times when the wall we're entering has its scan at index 0
#in other words, we don't really need to store and update wall position, but it's a cute naive soln
def moveAndScan(wallSpecs, wallLength):
    delay = findStealthDelay(wallSpecs)
    scanPos = {k:(-abs((delay%(2 * (wallSpecs[k]-1)))-(wallSpecs[k]-1)) - 1) for k in wallSpecs.keys()}
    myDepth = -1
    severity = 0
    for picoSec in range(delay, delay+wallLength):
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

def findStealthDelay(wallSpecs):
    def testDelay(wallSpecs, delay):
        for wallDepth in wallSpecs:
            if (delay+wallDepth) % (2*wallSpecs[wallDepth] - 2) == 0:
                return False
        return True
    delay = 1 #a delay of 0 will always get caught at wallDepth 0 if a wall exists there
    isDelaySuccessful = False
    while isDelaySuccessful == False:
        isDelaySuccessful = testDelay(wallSpecs, delay)
        if isDelaySuccessful == False:
            delay += 1
    print("Delayed {} picoseconds".format(delay))
    return delay

if __name__ == "__main__":
    main()