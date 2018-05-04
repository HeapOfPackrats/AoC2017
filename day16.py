#http://adventofcode.com/2017/day/16
#16 "programs" named "a" through "p" start in 0-indexed alphabetical order
#these programs go through a sequence of dance moves:
#   spin (sX): X programs move from the end to the front, maintaining order
#   exchange (xA/B): programs at positions A and B swap places
#   partner (pA/B): programs named A and B swap places
#we report the order of the programs after they've finished their dance

def main():
    movesList = getMoves("input16.txt")
    dancerList = list((chr(97+i) for i in range(16)))
    print("After the dance, the programs are in the following order: {}".format("".join(doDance(movesList, dancerList))))

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

if __name__ == "__main__":
    main()