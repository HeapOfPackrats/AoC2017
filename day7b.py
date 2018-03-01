#http://adventofcode.com/2017/day/7

import re
import itertools

def main():
    inputFile = open("input7.txt")
    #see url at top for specifications
    #first: build tree and a table of weights
    #second: recurse through tree, summing and comparing branch weights
    children = dict()
    nodeWeights = dict()
    ROOT = "mkxke"

    for line in inputFile:
        children.update(parseNodes(line))
        nodeWeights.update(parseWeights(line))
    inputFile.close()

    findImbalance(ROOT, children, nodeWeights)
    
#return node and any children as {node:[children]}
def parseNodes(line):
    #leaf nodes are distinguished by empty children list []
    names = list(filter(None, re.split("[^a-zA-Z]", line)))
    node = names[0]
    if len(names) > 1:
        children = names[1:]
    else:
        children = []
    return {node: children}

#return node and its weight as {node:weight}
def parseWeights(line):
    splitLine = line.split(maxsplit=2)
    node, weight = splitLine[0], splitLine[1]
    #format weight string '(##)' as int
    weight = int(weight[1:-1])
    return {node: weight}

#compare weights of all branches off of root node
#find the branch weight that's imbalanced relative to others, determine incorrectly weighted node and a new weight to balance node
def findImbalance(root, children, nodeWeights):
    #copy nodeWeights initially, update with weight of full branch
    #shallow copy is fine here since values are immutable
    branchWeights = dict(nodeWeights)
    imbalNode = dict(incorrect="", difference=0) #node (str), int
    sumBranchWeight(root, children, nodeWeights, branchWeights, imbalNode)
    
    if imbalNode["difference"] < 0:
        print("Program {}'s weight must be increased from {} to {}".format(imbalNode["incorrect"], nodeWeights[imbalNode["incorrect"]], nodeWeights[imbalNode["incorrect"]]-imbalNode["difference"]))
    elif imbalNode["difference"] > 0:
        print("Program {}'s weight must be decreased from {} to {}".format(imbalNode["incorrect"], nodeWeights[imbalNode["incorrect"]], nodeWeights[imbalNode["incorrect"]]-imbalNode["difference"]))

#recurse through a branch and sum weights until we find an imbalance
def sumBranchWeight(node, children, nodeWeights, branchWeights, imbalNode):
    for child in children[node]:
        if imbalNode["incorrect"] != "":
            break
        #if child is not leaf (i.e. has children), recurse up branch until node's child is a leaf
        if children[child]:
            sumBranchWeight(child, children, nodeWeights, branchWeights, imbalNode)
        #add weight of leaf or updated branchWeight[child]
        branchWeights[node] += branchWeights[child]

    if imbalNode["incorrect"] == "":
        compareChildren(node, children, branchWeights, imbalNode)

#compare branchWeight of children, determine any corrections to be made if imbalance is found
def compareChildren(node, children, branchWeights, imbalNode):
        balWeight, greater, lesser = None, None, None
        for a, b in itertools.combinations(children[node], 2):
            if branchWeights[a] == branchWeights[b]:
                balWeight = branchWeights[a]
            elif branchWeights[a] < branchWeights[b]:
                lesser, greater = a, b
            elif branchWeights[a] > branchWeights[b]:        
                greater, lesser = b, a
            if balWeight and greater and lesser:
                if balWeight == branchWeights[greater]:
                    imbalNode.update(incorrect=lesser, difference=branchWeights[lesser]-branchWeights[greater])
                elif balWeight == branchWeights[lesser]:
                    imbalNode.update(incorrect=greater, difference=branchWeights[greater]-branchWeights[lesser])
                break

if __name__ == "__main__":
    main()