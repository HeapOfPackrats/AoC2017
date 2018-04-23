#http://adventofcode.com/2017/day/12

#see url at top for full specifications
#given a list of "programs" (all with name="[0-9]*") and their connections to other "programs"
#find how many programs are connected (directly or indirectly) to program "0"

def main():
    with open("input12.txt") as inputFile:
        connections = parseConnects(inputFile)

    count, knownConnectsTo0 = countConnectsTo0(connections)
    print("These programs connect to program 0: {}".format(knownConnectsTo0))
    print("There are {} programs with direct or indirect connections to program 0".format(count))

#parse file into dictionary of programs (key) and a set of connected programs (value)
def parseConnects(inputFile):
    connections = dict()
    for line in inputFile:
        line = line.split(sep=" <-> ") #[k, "v1, v2, v3\n"]
        k, v = int(line[0]), set(map(int, line[1].strip().split(sep=", ")))
        connections.update({k:v}) #{k:[v1, v2, etc.]}
    return connections

#for each program, recurse through trees of connections to see if program 0 is connected
def doesConnectTo0(connections, knownConnectsTo0, program, checked=None):
    if checked is None: 
        checked = set() #setting a new pointer for each call from countConnectsTo0() as per https://reinout.vanrees.org/weblog/2012/04/18/default-parameters.html
    doesConnect = False
    #special case for program 0
    if program == 0: 
        for v in connections[0]:
            knownConnectsTo0.add(v) #all programs that 0 is connected to are also connected to 0
        doesConnect = True #program 0 is connected to itself
    else:
        if 0 in connections[program]:
            doesConnect = True
        else:
            for v in connections[program]:
                if doesConnect:
                    knownConnectsTo0.add(v)
                    break #just one connection to 0 is sufficient. Don't need to check other paths
                elif v in knownConnectsTo0:
                    doesConnect = True
                else:
                    if v == program or v in checked: 
                        continue #avoid looping within current program or back to previously checked
                    else:
                        checked.add(program)
                        doesConnect = doesConnectTo0(connections, knownConnectsTo0, v, checked)
    return doesConnect

#iterate through list of programs and determine which and how many connect to 0
def countConnectsTo0(connections):
    knownConnectsTo0 = set() #set of programs confirmed to connect to program 0
    count = 0
    for program in connections.keys():
        if doesConnectTo0(connections, knownConnectsTo0, program):
            knownConnectsTo0.add(program)
            count += 1
    return count, sorted(knownConnectsTo0)

if __name__ == "__main__":
    main()