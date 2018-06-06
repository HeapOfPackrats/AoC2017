#http://adventofcode.com/2017/day/24
#we wish to build a bridge out of components that each have two ports.
#each port has some number of pins, and connections can only be made between
#ports with the same number of pins.
#also, the bridge must start with a port with 0 pins, and each port on a
#component may only be used once.
#given a list of components, we wish to build a bridge with the highest
#possible number of pins

#for part 2, we wish to build the longest bridge possible. If multiple bridges
#are the same length, we want the strongest one

import time

def main():
    with open("input24.txt") as inputFile:
        start = time.time()
        components = getComponentsFromFile(inputFile)
    print("File: {} sec".format(time.time()-start))
    bridgeTrie = buildBridges(components)
    print("bridgeTrie: {} sec".format(time.time()-start))
    strongestLongest = findStrongestLongestBridge(components, bridgeTrie)
    print("strongestLongest: {} sec".format(time.time()-start))
    strongestLongestComponents = [list(map(str, components[comp])) for comp in strongestLongest]
    strongestLongestComponents = ", ".join(["/".join(n) for n in strongestLongestComponents])
    strongestLongestPinCount = sum([sum(components[comp]) for comp in strongestLongest])
    strongestLongestLength = len(strongestLongest)
    print("The bridge made of components {} is the strongest of the longest with length {} and strength {}".format(strongestLongestComponents, strongestLongestLength, strongestLongestPinCount))

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
def findStrongestLongestBridge(components, bridgeTrie, bridge=None, longest=None):
    if bridge is None:
        bridge = tuple()
        longest = list()
    if bridgeTrie:
        for component in bridgeTrie:
            longest = findStrongestLongestBridge(components, bridgeTrie[component], bridge + (component,), longest)
    else:
        if len(bridge) > len(longest):
            longest = list(bridge)
        elif len(bridge) == len(longest):
            bridgePins = sum([sum(components[comp]) for comp in bridge])
            strongestPins = sum([sum(components[comp]) for comp in longest])
            if bridgePins > strongestPins:
                longest = list(bridge)
    return longest

if __name__ == "__main__":
    main()