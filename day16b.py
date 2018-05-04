#http://adventofcode.com/2017/day/16
#16 "programs" named "a" through "p" start in 0-indexed alphabetical order
#these programs go through a sequence of dance moves:
#   spin (sX): X programs move from the end to the front, maintaining order
#   exchange (xA/B): programs at positions A and B swap places
#   partner (pA/B): programs named A and B swap places
#we report the order of the programs after they've finished their dance

#for part 2, we report the order after the programs perform a billion dances
#program order is retained between each instance of the dance

def main():
    movesList = getMoves("input16.txt")
    dancerList = list((chr(97+i) for i in range(16)))
    cycleLen = findCycleLen(movesList, dancerList)
    for i in range(1000000000%cycleLen):
        dancerList = doDance(movesList,dancerList)
    print("After the dance, the programs are in the following order: {}".format("".join(dancerList)))

def getMoves(filePath):
    with open(filePath) as movesFile:
        movesList = movesFile.read().split(sep=",")
    return movesList

def doDance(movesList, dancerList):
    dancerPos = dict()
    dancerCount = len(dancerList)
    for dancer, index in zip(dancerList, range(dancerCount)):
        dancerPos.update({dancer: index})
    for move in movesList:
        if move[0] == "s":
            x = int(move[1:])
            end = dancerList[-x:]
            front = dancerList[:-x]
            dancerList = end + front
            for dancer in dancerPos:
                dancerPos[dancer] = (dancerPos[dancer] + x) % dancerCount
        elif move[0] == "x":
            a, b = map(int, move[1:].split(sep="/"))          
            temp = dancerList[a]
            dancerList[a] = dancerList[b]
            dancerList[b] = temp
            dancerPos[dancerList[a]] = a
            dancerPos[dancerList[b]] = b
        elif move[0] == "p":
            a, b = move[1:].split(sep="/")
            temp = dancerPos[a]
            dancerPos[a] = dancerPos[b]
            dancerPos[b] = temp
            dancerList[dancerPos[a]] = a
            dancerList[dancerPos[b]] = b
    return dancerList

#finds the cycle length for the total dance permutation to restore
#the order of the programs to the original order
def findCycleLen(movesList, dancerList):
    dancerPermutations = set()
    dancerPermutations.add("".join(dancerList))
    for i in range(1, 5461): #see https://www.reddit.com/r/adventofcode/comments/7k5mrq/spoilers_in_title2017_day_16_part_2_cycles/drcb51m/
        dancerList = doDance(movesList, dancerList)
        permutation = "".join(dancerList)
        if permutation in dancerPermutations:
            return i
        else:
            dancerPermutations.add(permutation)

if __name__ == "__main__":
    main()