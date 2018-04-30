#http://adventofcode.com/2017/day/15
#see URL for full specifications
#two "generators" A and B both generate values by multiplying previous values
#values by given factors (A: 16807, B: 48271) then dividing their respective
#products by 2147483647. The first values are generated with starting values
#provided as puzzle inputs.
#we count how many pairs of values from A and B match in their first 16 bits
#after generating 40 million pairs

#for part b, each generator now functions independently and will not hand
#a value to the judge until it meets a divisibility criteria
#also, judge now only compares 5 million pairs

def main():
    puzzleInput = getPuzzleInput("input15.txt")
    A = makeGenerator(puzzleInput["A"], 16807, 4)
    B = makeGenerator(puzzleInput["B"], 48271, 8)
    print("There are {} matching pairs".format(judgeVals(A, B, 5000000)))

def getPuzzleInput(filePath):
    puzzleInput = dict()
    with open(filePath) as inputFile:
        #line = "Generator C starts with #", C = some Char, # = some integer
        for line in inputFile:
            genName = line[10]
            startVal = int(line[24:])
            puzzleInput.update({genName: startVal})
    return puzzleInput

def makeGenerator(startVal, factor, divisor):
    val = startVal
    def generate():
        nonlocal val
        while True:
            #Mersenne prime mod optimization on next three lines thanks to
            #https://www.reddit.com/r/adventofcode/comments/7jyz5x/2017_day_15_opportunities_for_optimization/drasfzr/
            val = (val*factor)
            val = (val & 0x7fffffff) + (val >> 31)
            val = val - 0x7fffffff if val >> 31 else val
            if val%divisor == 0:
                break
        return val
    return generate

def judgeVals(genA, genB, iterations):
    count = 0
    for i in range(iterations):
        if genA() & 0xffff == genB() & 0xffff:
            count += 1
    return count

if __name__ == "__main__":
    main()