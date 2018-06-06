#http://adventofcode.com/2017/day/25
#we are given an infinite tape of 0 repeated infinitely in both directions,
#a cursor that moves l/r along the tape and writes values at its current
#position, and a set of states (the puzzle input) which instruct the cursor 
#depending on the value under the cursor.
#we wish to report the state of the tape (its sum) after carrying out the
#instructions on our input

from collections import deque
import re

def main():
    with open("input25.txt") as inputFile:
        beginState, diagSteps, states = getBlueprintFromFile(inputFile)
    doDiagnostic(beginState, diagSteps, states)

#returns three items: the state to begin with, the number of diagnostic steps
#to perform, and the states as a dict
def getBlueprintFromFile(inputFile):
    beginP = re.compile("(?:Begin in state) (\w+)")
    diagP = re.compile("(?:checksum after) (\w+)")
    stateP = re.compile("(?:In state) (\w+)(?:.|\n)*?(?:If the current value is) (\w+)(?:.|\n)*?(?:Write the value) (\w+)(?:.|\n)*?(?:Move one slot to the) (\w+)(?:.|\n)*?(?:Continue with state) (\w+)(?:.|\n)*?(?:If the current value is) (\w+)(?:.|\n)*?(?:Write the value) (\w+)(?:.|\n)*?(?:Move one slot to the) (\w+)(?:.|\n)*?(?:Continue with state) (\w+)")
    inputText = inputFile.read()
    #get initial state and number of diagnostic steps to iterate
    beginState = beginP.search(inputText).group(1)
    diagSteps = int(diagP.search(inputText).group(1))
    #retreive states
    statesList = stateP.findall(inputText)
    states = dict()
    for state in statesList:
        name = state[0] 
        cond1, write1, move1, cont1 = state[1:5]
        cond2, write2, move2, cont2 = state[5:9]
        #example: {'A', {0: [1, 'right', 'B'], 1: [0, 'left', 'B']}}
        states.update({name: {int(cond1): {"write": int(write1), "move": move1, "continue": cont1}, int(cond2): {"write": int(write2), "move": move2, "continue": cont2}}})
    return beginState, diagSteps, states

#perform diagnostic, print diagnostic checksum
def doDiagnostic(beginState, diagSteps, states):
    #initialize tape
    tape = deque([0 for i in range(1000)])
    #initialize cursor at "middle" of "infinite" tape
    cursor = 499
    #initialize state
    state = beginState
    #perform diagnostic for diagSteps iterations
    for _ in range(diagSteps):
        #retrieve tape value at cursor
        currVal = tape[cursor]
        #write to tape according to state
        tape[cursor] = states[state][currVal]["write"]
        #update cursor
        if states[state][currVal]["move"] == "right":
            cursor += 1
        else:
            cursor = (cursor - 1)%len(tape)
        #expand "infinite" tape as needed
        if cursor == 0:
            tape.appendleft(0)
            cursor += 1
        elif cursor == len(tape):    
            tape.append(0)
        #move to next state
        state = states[state][currVal]["continue"]
    print("The diagnostic produced a checksum of {}".format(sum(tape)))

if __name__ == "__main__":
    main()