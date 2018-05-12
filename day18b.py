#http://adventofcode.com/2017/day/18
#we have a list of registers which each hold a single int and 
#are named with a single letter.
#each register starts with an int value of 0.
#we run an assembly of instructions (our puzzle input) on
#the list of registers (see url for instruction specifications).
#we wish to find the value of the first successfully-executed
#rcv instruction

#for part 2, we found out that the instructions are meant to be 
#run in twice in parallel (id=0,1; register p initialized to respective id).
#the snd and rcv messages are actually used to coordinate: 
#"snd x" sends the value of x to a queue to be read by the other program,
#"rcv x" receives the next queued value and stores it in register x.
#Programs pause until they've receieved a value, and values are receieved
#in order that they are sent.
#when both programs try unsuccessfully to rcv while no data is queued,
#they deadlock and both terminate.
#we wish to know how many times program 1 sends values before the programs
#terminate

import queue
from multiprocessing import Manager, Queue, Pool

def main():
    with open("input18.txt") as inputFile:
        instructions = getInstructions(inputFile)
    m = Manager() #https://stackoverflow.com/a/9928191
    q0to1 = m.Queue()
    q1to0 = m.Queue()
    pool = Pool(processes=2) #http://www.dabeaz.com/usenix2009/concurrent/Concurrent.pdf
    prog0 = pool.apply_async(doInstructions, (instructions, 0, q0to1, q1to0))
    prog1 = pool.apply_async(doInstructions, (instructions, 1, q1to0, q0to1))
    print("Program {0[0]} sent values {0[1]} times".format(prog0.get()))
    print("Program {0[0]} sent values {0[1]} times".format(prog1.get()))

def buildRegisters():
    registers = {chr(i):0 for i in range(97,97+26)}
    return registers

def getInstructions(inputFile):
    instructions = [line.strip().split(sep=" ") for line in inputFile]
    return instructions

#do instructions in parallel with another process,
#track and return how many values are sent
def doInstructions(instructions, progID, sndQueue, rcvQueue):
    registers = buildRegisters()
    registers["p"] = progID
    sndCount = 0

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
            sndQueue.put(getVal(x))
            sndCount += 1
        elif instruction == "set":
            registers[x] = getVal(y)
        elif instruction == "add":
            registers[x] += getVal(y)
        elif instruction == "mul":
            registers[x] *= getVal(y)
        elif instruction == "mod":
            registers[x] = getVal(x) % getVal(y)
        elif instruction == "rcv":
            try:
                registers[x] = rcvQueue.get(timeout=5)
            except queue.Empty:
                return (progID, sndCount)
        elif instruction == "jgz":
            if getVal(x) > 0:
                i += getVal(y)
                continue
        i += 1

if __name__ == "__main__":
    main()