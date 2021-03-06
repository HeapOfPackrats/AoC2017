#http://adventofcode.com/2017/day/22
#we are given a map of nodes that details the infection state of each node.
#a "virus carrier" starts in the middle of the map facing up and does the 
#following for each "burst" of activity:
# if current node is infected, turn right. Else, turn left;
# if current node is infected, clean the node. Else, infect it;
# move forward along the direction it's facing.
#we wish to know how many bursts out of the first 10000 were spent
#causing infections

#for part 2, the virus carrier has additional behaviors and flags nodes:
# Clean nodes become weakened;
# Weakened nodes become infected;
# Infected nodes become flagged;
# Flagged nodes become clean.
#the virus carrier movement depends on these flags:
# If it is clean, it turns left;
# If it is weakened, it does not turn;
# If it is infected, it turns right;
# If it is flagged, it reverses direction.
#we wish to know how many bursts out of the first 10000000 are spent
#causing infections

def main():
    with open("input22.txt") as inputFile:
        map = getMapFromFile(inputFile)
    doBurst(map, iterations=10000000)

#returns a 2D array of "." and "#" (a "map")
#up and left are negative directions, down and right are positive
#the "map" is composed of "clean nodes" (denoted by ".") and infected ("#")
def getMapFromFile(inputFile):
    map = list()
    for line in inputFile:
        map.append(list(line.strip()))
    return map

#modifies map per the behavior outlined for the "virus carrier"
#prints the total number of burst iterations and number of bursts in which
#"infection" occured 
def doBurst(map, iterations=1):
    #start in middle of map, facing upward
    posX = int(len(map[0])/2)
    posY = int(len(map)/2)
    moveX = 0
    moveY = -1
    #track number of infections caused
    infectionsCaused = 0
    #do bursts for specified number of iterations
    for _ in range(iterations):
        #infect/weaken/flag/disinfect node and pick a relative direction 
        #to turn (left, straight, right, reverse, respectively)
        if map[posY][posX] == ".":
            direction = "left"
            map[posY][posX] = "w"
        elif map[posY][posX] == "w":
            direction = "straight"
            map[posY][posX] = "#"
            infectionsCaused += 1
        elif map[posY][posX] == "#":
            direction = "right"
            map[posY][posX] = "f"
        elif map[posY][posX] == "f":
            direction = "reverse"
            map[posY][posX] = "."
        #determine heading on map (up, down left, right)
        if direction == "reverse":
            moveX *= -1
            moveY *= -1
        elif direction == "straight":
            pass
        elif moveY != 0:
            if direction == "right":
                moveX -= moveY
                moveY = 0
            elif direction == "left":
                moveX += moveY
                moveY = 0        
        elif moveX != 0:
            if direction == "right":
                moveY += moveX
            elif direction == "left":
                moveY -= moveX
            moveX = 0
        #move, expand map as needed
        posX += moveX
        posY += moveY
        if not 0 <= posX < len(map[0]):
            if moveX > 0:
                for row in map:
                    row.append(".")
            elif moveX < 0:
                for row in map:
                    row.insert(0, ".")
                posX = 0
        if not 0 <= posY < len(map):
            newRow = ["." for i in range(len(map[0]))]
            if moveY > 0:
                map.append(newRow)
            elif moveY < 0:
                map.insert(0, newRow)
                posY = 0
    print("Of {} bursts, {} caused a node to become infected".format(iterations, infectionsCaused))
    
if __name__ == "__main__":
    main()