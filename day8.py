#http://adventofcode.com/2017/day/8

def main():
    #see url at top for full specifications
    #read in a list of registers and their instructions
    #store+modify registers in order of first to last according to their instructions

    with open("input8.txt") as inputFile:
        regVals = dict()
        execInstructions(inputFile, regVals)

    highestReg, highestVal = findHighest(regVals)
    print("Register {} has the highest value, {}".format(highestReg, highestVal))

def execInstructions(inputFile, regVals):
    for line in inputFile:
        line = line.split()
        reg, incOrDec, amt, regComp, cond, val = line[0], line[1], int(line[2]), line[4], line[5], int(line[6])
        #check conditional statement first
        if reg not in regVals:
            regVals.update({reg: 0})
        if regComp not in regVals:
            regVals.update({regComp: 0})
        if tOrF(regVals[regComp], cond, val):
            if incOrDec == "inc":
                regVals[reg] += amt
            elif incOrDec == "dec":
                regVals[reg] -= amt

def tOrF(regVal, cond, val):
    if cond == "<":
        isTorF = (regVal < val)
    elif cond == "<=":
        isTorF = (regVal <= val)
    elif cond == ">":
        isTorF = (regVal > val)
    elif cond == ">=":
        isTorF = (regVal >= val)
    elif cond == "==":
        isTorF = (regVal == val)
    elif cond == "!=":
        isTorF = (regVal != val)
    return isTorF

def findHighest(regVals):
    highestReg = ""
    highestVal = 0
    for reg in regVals:
        if regVals[reg] > highestVal:
            highestReg = reg
            highestVal = regVals[reg]
    return highestReg, highestVal

if __name__ == "__main__":
    main()