#http://adventofcode.com/2017/day/7

import re

def main():
    inputFile = open("input7.txt")

    #see url at top for specifications
    #build sets of all nodes and of all children nodes, subtract sets to find root node

    nodeSet = set()
    childrenSet = set()

    for line in inputFile:
        node, children = parseIntoNodes(line)
        nodeSet.add(node)
        childrenSet.update(children)

    inputFile.close()
    print("{} is the root node".format(nodeSet-childrenSet))
    
def parseIntoNodes(line):
    names = list(filter(None, re.split("[^a-zA-Z]", line)))
    node = names[0]
    if len(names) > 1:
        children = names[1:]
    else:
        children = []
    return node, children

if __name__ == "__main__":
    main()