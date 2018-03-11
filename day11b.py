#http://adventofcode.com/2017/day/11

#see url at top for full specifications
#given a list of 6 vectors/steps (n, nw, ne, s, sw, se) in a hex grid
#find net displacement of "child process" (shortest distance to end)
#also find max displacement of "child"

def main():
    with open("input11.txt") as inputFile:
        steps = inputFile.read().split(sep=",")
    net = netSteps(steps)
    print("The child process is {} steps away".format(int(net["sum"])))
    print("The maximum displacement of the child process is {} steps".format(int(maxDisplacement(steps))))

#calc net steps
def netSteps(steps):
    vectors = dict(n=0, w=0, e=0, s=0)
    for step in steps:
        if step == "n" or step == "s":
            #pure n/s movement is 2x the n/s movement of nw/ne/etc
            vectors[step] += 2
        else:
            for vector in step:
                vectors[vector] += 1
    netSteps = dict(n=0, nw=0, ne=0, s=0, sw=0, se=0, sum=0)
    #find net movement with n,s,e,w mapped to cartesian: n & e pos, s & w neg
    diffNS = vectors["n"] - vectors["s"]
    diffEW = vectors["e"] - vectors["w"]

    if diffNS >= 0: #net north or no movement n/s
        if diffEW > 0: #net east
            if diffEW >= diffNS: #no n steps, all n/s is from ne/se steps 
                netSteps["ne"] = diffNS
                netSteps["se"] = diffEW - diffNS
                netSteps["sum"] =  netSteps["ne"] + netSteps["se"]
            else:               #some n steps, 0 or more ne steps
                netSteps["n"] = (diffNS - diffEW)*0.5
                netSteps["ne"] = diffEW
                netSteps["sum"] =  netSteps["n"] + netSteps["ne"]
        else:          #net west or no net e/w movement
            diffEW = abs(diffEW)
            if diffEW >= diffNS: 
                netSteps["nw"] = diffNS
                netSteps["sw"] = diffEW - diffNS
                netSteps["sum"] =  netSteps["nw"] + netSteps["sw"]
            else:               
                netSteps["n"] = (diffNS - diffEW)*0.5
                netSteps["nw"] = diffEW
                netSteps["sum"] = netSteps["n"] + netSteps["nw"]
    else:           # net south
        diffNS = abs(diffNS)
        if diffEW > 0:
            if diffEW >= diffNS: 
                netSteps["se"] = diffNS
                netSteps["ne"] = diffEW-diffNS
                netSteps["sum"] =  netSteps["ne"] + netSteps["se"]
            else:              
                netSteps["s"] = (diffNS - diffEW)*0.5
                netSteps["sw"] = diffEW
                netSteps["sum"] =  netSteps["s"] + netSteps["sw"]
        else:         
            diffEW = abs(diffEW)
            if diffEW >= diffNS:
                netSteps["sw"] = diffNS
                netSteps["nw"] = diffEW-diffNS
                netSteps["sum"] =  netSteps["nw"] + netSteps["sw"]
            else:               
                netSteps["s"] = (diffNS - diffEW)*0.5
                netSteps["sw"] = diffEW
                netSteps["sum"] =  netSteps["s"] + netSteps["sw"]
    return netSteps

#calculate max displacement at any point
def maxDisplacement(steps):
    maxD = 0
    for i in range(1, len(steps)):
        curr = netSteps(steps[:i])
        if curr["sum"] > maxD:
            maxD = curr["sum"]
    return maxD

if __name__ == "__main__":
    main()