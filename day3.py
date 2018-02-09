#http://adventofcode.com/2017/day/3

import sys

def main(argv):
    #get input, otherwise prompt for input
    if (len(argv) == 2):
        inputSquare = int(argv[1])
    else:
        print("Please specify an input argument (day3.py [input])")
        return

    #find Manhattan Distance from square # specified by input to square 1 at the center
    #refer to url at top for diagram

    #check which layer box the input square resides in
    n = int(0.5*((inputSquare-1)**0.5 + 1))

    #calc box geometry
    #note: minVal doesn't actually appear on any given layer and is just for calculating geometry
    #note: maxVal overlaps lowerRight
    minVal = (2*n-1)**2
    maxVal = (2*n+1)**2
    lowerRight = minVal
    upperRight = minVal + 2*n
    upperLeft = minVal + 4*n
    lowerLeft = minVal + 6*n
    midRight = lowerRight + n
    midTop = upperRight + n
    midLeft = upperLeft + n
    midBottom = lowerLeft + n

    #check which side of the box the square is on, find distance to middle of side
    if lowerRight < inputSquare <= upperRight:
        toCenter = "left"
        distance = midRight - inputSquare

        if distance < 0:
            initialMove = "down"
            distance *= -1
        elif distance > 0:
            initialMove = "up"
        else:
            initialMove = "none"

    elif upperRight < inputSquare <= upperLeft:
        toCenter = "down"
        distance = midTop - inputSquare

        if distance < 0:
            initialMove = "right"
            distance *= -1
        elif distance > 0:
            initialMove = "left"
        else:
            initialMove = "none"
    
    elif upperLeft < inputSquare <= lowerLeft:
        toCenter = "right"
        distance = midLeft - inputSquare

        if distance < 0:
            initialMove = "up"
            distance *= -1
        elif distance > 0:
            initialMove = "down"
        else:
            initialMove = "none"

    elif lowerLeft < inputSquare <= maxVal:
        toCenter = "up"
        distance = midBottom - inputSquare

        if distance < 0:
            initialMove = "left"
            distance *= -1
        elif distance > 0:
            initialMove = "right"
        else:
            initialMove = "none"

    #print total steps
    if initialMove == "none":
        print("{} step(s) {}. Total of {} steps".format(n, toCenter, distance+n))
    else:
        print("{} step(s) {}, then {} step(s) {}. Total of {} steps".format(distance, initialMove, n, toCenter, distance+n))

if __name__ == "__main__":
    main(sys.argv)