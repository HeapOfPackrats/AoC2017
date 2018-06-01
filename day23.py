#http://adventofcode.com/2017/day/23
#we have a list of registers which each hold a single int and 
#are named with a single letter.
#each register starts with an int value of 0.
#we run an assembly of instructions (our puzzle input) on
#the list of registers (see url for instruction specifications).
#we wish to find the number of times the "mul" instruction is invoked

def main():
    with open("input23.txt") as inputFile:
        instructions = getInstructionsFromFile(inputFile)
    doInstructions(instructions)

#returns a set of registers a through h, each initialized to 0
def buildRegisters():
    registers = {chr(i):0 for i in range(97,97+8)}
    return registers

def getInstructionsFromFile(inputFile):
    instructions = [line.strip().split(sep=" ") for line in inputFile]
    return instructions

#do instructions and print how many mul instructions are executed
def doInstructions(instructions):
    registers = buildRegisters()
    mulCount = 0

    def getVal(s):
        try:
            return registers[s]
        except KeyError:
            return int(s)
    
    i = 0
    while 0 <= i < len(instructions):
        if len(instructions[i]) == 3:
            instruction, x, y = instructions[i]
        elif len(instructions[i]) == 2:
            instruction, x = instructions[i]
        else:
            continue
        if instruction == "set":
            registers[x] = getVal(y)
        elif instruction == "sub":
            registers[x] -= getVal(y)
        elif instruction == "mul":
            registers[x] *= getVal(y)
            mulCount += 1
        elif instruction == "jnz":
            if getVal(x) != 0:
                i += getVal(y)
                continue
        i += 1
    print("The mul instructions was invoked {} times".format(mulCount))

if __name__ == "__main__":
    main()