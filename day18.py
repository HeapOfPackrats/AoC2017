#http://adventofcode.com/2017/day/18
#we have a list of registers which each hold a single int and 
#are named with a single letter.
#each register starts with an int value of 0.
#we run an assembly of instructions (our puzzle input) on
#the list of registers (see url for instruction specifications).
#we wish to find the value of the first successfully-executed
#rcv instruction

def main():
    registers = buildRegisters()
    with open("input18.txt") as inputFile:
        instructions = getInstructions(inputFile)
    duet = doInstructions(instructions, registers)
    print("The first recovered frequency is {}".format(duet[1][0]))

def buildRegisters():
    registers = {chr(i):0 for i in range(97,97+26)}
    return registers

def getInstructions(inputFile):
    instructions = [line.strip().split(sep=" ") for line in inputFile]
    return instructions

#do instructions, return the sequence of frequencies played by
#instructions "snd" and "rcv" (tuple duet)
def doInstructions(instructions, registers):
    sndSong = list()
    rcvSong = list()
    duet = (sndSong, rcvSong)

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

        if instruction == "snd":
            sndSong.append(getVal(x))
        elif instruction == "set":
            registers[x] = getVal(y)
        elif instruction == "add":
            registers[x] += getVal(y)
        elif instruction == "mul":
            registers[x] *= getVal(y)
        elif instruction == "mod":
            registers[x] = getVal(x) % getVal(y)
        elif instruction == "rcv":
            if getVal(x) != 0 and sndSong:
                rcvSong.append(sndSong[-1])
                return duet
        elif instruction == "jgz":
            if getVal(x) > 0:
                i += getVal(y)
                continue
        i += 1
    return duet

if __name__ == "__main__":
    main()