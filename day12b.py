#http://adventofcode.com/2017/day/12

#see url at top for full specifications
#given a list of "programs" (all with name="[0-9]*") and their connections to other "programs"
#and given that a "group" is a set of programs connected to a particular group
#find how many different groups exist within a list of connections

from collections import OrderedDict 

def main():
    with open("input12.txt") as inputFile:
        connections = parseConnects(inputFile)
    groups = buildGroups(connections)
    for group in groups.items():
        print(group)
    print("There are {} distinct groups of programs".format(len(groups)))

#parse file into dictionary of programs (key) and a set of connected programs (value)
def parseConnects(inputFile):
    connections = OrderedDict()
    for line in inputFile:
        line = line.split(sep=" <-> ") #[k, "v1, v2, v3\n"]
        k, v = int(line[0]), set(map(int, line[1].strip().split(sep=", ")))
        connections.update({k:v}) #{k:[v1, v2, etc.]}
    return connections

#for each program which starts a group and has neighbors, recurse through neighbors to gather group members
def findGroupMembers(connections, groups, groupName, program, checked=None):
    if checked is None:
        checked = set({groupName}) #setting a new pointer for each call from buildGroups() as per https://reinout.vanrees.org/weblog/2012/04/18/default-parameters.html
    for connection in connections[program]:
        if connection != groupName and connection not in checked:
            checked.add(connection)
            findGroupMembers(connections, groups, groupName, connection, checked)
            groups[groupName].add(connection)

#iterate through list of programs and determine distinct groups of interconnected programs
def buildGroups(connections):
    groups = dict()
    grouped = set()
    for program in connections.keys():
        if program in grouped:
            continue
        else:
            if connections[program] == {program}: #program has only itself in its group. Don't attempt to find neighbors
                groups.update({program: program})
            else: 
                groups.update({program: set()})
                findGroupMembers(connections, groups, program, program)
                grouped.update(groups[program])
    return groups

if __name__ == "__main__":
    main()