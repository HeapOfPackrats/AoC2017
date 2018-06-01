#http://adventofcode.com/2017/day/23
#we have a list of registers which each hold a single int and 
#are named with a single letter.
#each register starts with an int value of 0.
#we run an assembly of instructions (our puzzle input) on
#the list of registers (see url for instruction specifications).
#we wish to find the number of times the "mul" instruction is invoked

#for part 2, we "turn off" the "debugger" by initializing register a to 1
#we wish to know what value is left in register h after running the program

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
#also print the value of register h after completion of instructions
def doInstructions(instructions):
    registers = buildRegisters()
    mulCount = 0
    #set register a to 1 to turn off "debug mode"
    registers["a"] = 1

    def getVal(s):
        try:
            return registers[s]
        except KeyError:
            return int(s)

    #refer to diagram of loop structure at bottom of file
    #the two inner loops together only have one purpose: to switch reg f on
    #or off.
    #the register that controls the innermost loop's exit condition, e, 
    #and the parent loop's control register, d, both are >= 2 and < b due to
    #the way the assembly is set up.
    #thus, it's sufficient to check divisibility of d from 2 to 0.5*b, and
    #the loops can otherwise be skipped
    def optimizeLoops(i, registers=registers):
        b = registers["b"]
        if i == 11:
            registers["e"] = b - 1
        elif i == 10:
            registers["d"] = b - 1
            for d in range(2, int(b/2) + 1):
                if b%d == 0:
                    registers["f"] = 0
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
                optimizeLoops(i)
                continue
        i += 1
    print("The mul instructions was invoked {} times".format(mulCount))
    print("Register h is left with the value {}".format(registers["h"]))

if __name__ == "__main__":
    main()

# 00    set b 84
# 01    set c b
# 02    jnz a 2 (GOTO 4. DEBUG SWITCH)
# 03    jnz 1 5 (GOTO 8. SKIPPED WHEN DEBUG OFF) 
# 04    mul b 100
# 05    sub b -100000
# 06    set c b
# 07    sub c -17000
# 08        set f 1
# 09        set d 2
# 10            set e 2
# 11                set g d
# 12                mul g e
# 13                sub g b
# 14                jnz g 2 (GOTO 16)
# 15                set f 0 (IMPORTANT LINE. f = 0 if (d*e)-b = 0)
# 16                sub e -1
# 17                set g e
# 18                sub g b
# 19                jnz g -8 (GOTO 11)
# 20            sub d -1
# 21            set g d
# 22            sub g b
# 23            jnz g -13 (GOTO 10)
# 24        jnz f 2 (GOTO 26)
# 25        sub h -1
# 26        set g b
# 27        sub g c
# 28        jnz g 2 (GOTO 30)
# 29        jnz 1 3 (END)
# 30        sub b -17
# 31        jnz 1 -23 (GOTO 8)