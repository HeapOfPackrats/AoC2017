#http://adventofcode.com/2017/day/24
#we wish to build a bridge out of components that each have two ports.
#each port has some number of pins, and connections can only be made between
#ports with the same number of pins.
#also, the bridge must start with a port with 0 pins, and each port on a
#component may only be used once.
#given a list of components, we wish to build a bridge with the highest
#possible number of pins

import time

def main():
    with open("input24.txt") as inputFile:
        start = time.time()
        components = getComponentsFromFile(inputFile)
    print("File: {} sec".format(time.time()-start))
    bridgeTrie = buildBridges(components)
    print("bridgeTrie: {} sec".format(time.time()-start))
    strongest = findStrongestBridge(components, bridgeTrie)
    print("Strongest: {} sec".format(time.time()-start))
    strongestComponents = [list(map(str, components[comp])) for comp in strongest]
    strongestComponents = ", ".join(["/".join(n) for n in strongestComponents])
    strongestPinCount = sum([sum(components[comp]) for comp in strongest])
    print("The bridge made of components {} has the highest pin count, {}".format(strongestComponents, strongestPinCount))

#return a list containing pairs of ports (components)
def getComponentsFromFile(inputFile):
    components = list()
    for line in inputFile: #example: line = "25/13"
        line = line.strip()
        lPort, rPort = map(int, line.split(sep="/"))
        components.append((lPort, rPort))
    return components

#return a trie of all possible bridges where each node is the index
#of the component in the list of components
def buildBridges(components, bridgeTrie=dict(), portToMatch=0, prev=tuple()):
    #make trie, start by finding base of trie (components with a 0-pin port)
    for componentID, component in enumerate(components):
        try:
            index = component.index(portToMatch)
            if componentID not in prev:
                bridgeTrie.update({componentID: dict()})
                buildBridges(components, bridgeTrie[componentID], component[index-1], prev + (componentID,))
        except ValueError:
            continue
    return bridgeTrie

#recurses down through bridge trie to calculate bridge strenghts.
#prints the components and the pin count of the bridge with the highest number
#of pins (the "strongest" bridge)
def findStrongestBridge(components, bridgeTrie, bridge=None, strongest=None):
    if bridge is None:
        bridge = tuple()
        strongest = list()
    if bridgeTrie:
        for component in bridgeTrie:
            strongest = findStrongestBridge(components, bridgeTrie[component], bridge + (component,), strongest)
    else:
        bridgePins = sum([sum(components[comp]) for comp in bridge])
        strongestPins = sum([sum(components[comp]) for comp in strongest])
        if bridgePins > strongestPins:
            strongest = list(bridge)
    return strongest

if __name__ == "__main__":
    main()