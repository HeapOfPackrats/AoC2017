#http://adventofcode.com/2017/day/20
#we're given a list of particles and their properties, including:
#position, velocity, and acceleration in the x, y, and z axes.
#all particles are updated simultaneously per tick in the following order:
#x, y, z velocities are increased by their relative accelerations, then
#x, y, z positions are updated by their updated velocities.
#we wish to know which particle will stay closest to coordinate (0, 0, 0)
#in the long term as measured by the Manhattan distance

#for part 2, we will remove particles that collide, i.e. occupy the same
#position after a tick.
#we wish to know how many particles remain after all collisions are resolved

import re

def main():
    with open("input20.txt") as inputFile:
        particles = getParticlesFromInput(inputFile)
    slowest = findSlowest(particles)
    print("In the long term, particle {} will be closest to (0, 0, 0)".format(slowest))
    collideParticles(particles)
    print("After all collisions are resolved, there are {} particles left".format(len(particles["positions"])))

#retrieve particle properties as normalized data in three dict for
#position, velocity, and acceleration
def getParticlesFromInput(inputFile):
    particlesP = dict()
    particlesV = dict()
    particlesA = dict()
    i = 0
    pattern = re.compile("<(.*?)>") #find all "<x,y,z>""
    for line in inputFile: #ex: "p=<1,2,3>, v=<4,5,6>, a=<7,8,9>"
        pva = pattern.findall(line) #ex: ["1,2,3", "4,5,6", "7,8,9"]
        p, v, a = [list(map(int,s.split(","))) for s in pva]
        particlesP.update({i: p})
        particlesV.update({i: v})
        particlesA.update({i: a})
        i += 1
    particles = {"positions": particlesP, "velocities": particlesV, "accelerations": particlesA}
    return particles

    #in the long run, the particle(s) closest to (0, 0, 0) will be the particle(s)
#with the smallest acceleration.
#if there are multiple with the same magnitude of Manhattan acceleration,
#sort by "agreement" between acceleration and initial velocity by taking the
#dot product but changing any product==zero to absolute value of the
#non-zero factor, and we assume this will resolve any ties that occur.
#findSlowest returns the particle which has the smallest acceleration
def findSlowest(particles):
    velocities = particles["velocities"]
    accelerations = particles["accelerations"]

    slowestID = 0
    slowestA = sum(map(abs,accelerations[0]))
    for i in range(1,len(accelerations)):
        a = sum(map(abs,accelerations[i]))
        if a < slowestA:
            slowestID = i
            slowestA = a
        elif a == slowestA:
            slowestAgreement = 0
            agreement = 0
            for x, y in zip(velocities[slowestID], accelerations[slowestID]):
                if x*y != 0:
                    slowestAgreement += x*y
                else:
                    slowestAgreement += abs(x) + abs(y)
            for x, y in zip(velocities[i], accelerations[i]):
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

#iteratively update particle velocities and positions and check for collisions.
#runs for an arbitrary number of iterations
def collideParticles(particles):
    positions = particles["positions"]
    velocities = particles["velocities"]
    accelerations = particles["accelerations"]

    collisionPosList = list()
    removeParticles = set()
    for _ in range(500):
        keys = list(positions.keys())
        for index, i in enumerate(keys):
            #update velocity
            velocities[i] = [v + a for v, a in zip(velocities[i], accelerations[i])]
            #update position
            positions[i] = [p + v for p, v in zip(positions[i], velocities[i])]
            #check for collisions, queue collided particles for removal
            for j in keys[:index]:
                if positions[i] in collisionPosList:
                    removeParticles.add(i)
                elif positions[j] == positions[i] and j != i:
                    collisionPosList.append(positions[j])
                    removeParticles.add(i)
                    removeParticles.add(j)
        for id in removeParticles:
            del positions[id]
            del velocities[id]
            del accelerations[id]
        removeParticles.clear()

if __name__ == "__main__":
    main()