#http://adventofcode.com/2017/day/20
#we're given a list of particles and their properties, including:
#position, velocity, and acceleration in the x, y, and z axes.
#all particles are updated simultaneously per tick in the following order:
#x, y, z velocities are increased by their relative accelerations, then
#x, y, z positions are updated by their updated velocities.
#we wish to know which particle will stay closest to coordinate (0, 0, 0)
#in the long term as measured by the Manhattan distance

import re

def main():
    with open("input20.txt") as inputFile:
        particles = getParticlesFromInput(inputFile)
    slowest = findSlowest(particles)
    print("In the long term, particle {} will be closest to (0, 0, 0)".format(slowest))

def getParticlesFromInput(inputFile):
    particles = dict()
    i = 0
    pattern = re.compile("<(.*?)>")
    for line in inputFile: #ex: "p=<1,2,3>, v=<4,5,6>, a=<7,8,9>"
        pva = pattern.findall(line) #ex: ["1,2,3", "4,5,6", "7,8,9"]
        p, v, a = [list(map(int,s.split(","))) for s in pva]
        particles.update({i: {"p":p, "v":v, "a":a}})
        i += 1
    return particles

#in the long run, the particle(s) closest to (0, 0, 0) will be the particle(s)
#with the smallest acceleration.
#if there are multiple with the same magnitude of Manhattan acceleration,
#sort by "agreement" between acceleration and initial velocity by taking the
#dot product but changing any product==zero to absolute value of the
#non-zero factor, and we assume this will resolve any ties that occur.
#findSlowest returns the particle which has the smallest acceleration
def findSlowest(particles):
    slowestID = 0
    slowestA = sum(map(abs,particles[0]["a"]))
    for i in range(1,len(particles)):
        a = sum(map(abs,particles[i]["a"]))
        if a < slowestA:
            slowestID = i
            slowestA = a
        elif a == slowestA:
            slowestAgreement = 0
            agreement = 0
            for x, y in zip(particles[slowestID]["v"], particles[slowestID]["a"]):
                if x*y != 0:
                    slowestAgreement += x*y
                else:
                    slowestAgreement += abs(x) + abs(y)
            for x, y in zip(particles[i]["v"], particles[i]["a"]):
                if x*y != 0:
                    agreement += x*y
                else:
                    agreement += abs(x) + abs(y)
            if agreement < slowestAgreement:
                slowestID = i
                slowestA = a
            else:
                continue
    return slowestID

if __name__ == "__main__":
    main()