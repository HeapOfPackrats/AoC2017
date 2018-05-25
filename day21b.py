#http://adventofcode.com/2017/day/21
#see url for the description of the pattern recognition/manipulation
#for day 21.
#we wish to see how many "#" we have after running five iterations of
#the pattern manipulation rules specified by the puzzle input

#for part 2, we run eighteen iterations

def main():
    with open("input21.txt") as inputFile:
        rules = getRulesFromFile(inputFile)
    pattern = doEnhancement(rules, iterations=18)
    onPixels = sum([row.count("#") for row in pattern])
    print("There are {} pixels that are on after 18 iterations of enhancement".format(onPixels))

#retrieve enhancement rules as a list of indexed patterns and output 2D lists
#return the rules
def getRulesFromFile(inputFile):
    rules = dict()
    for i, line in enumerate(inputFile):
        line = line.strip() #ex: "#.#/#../..." => "...#/#.##/####/##.#"
        pattern, output = line.split(sep=" => ", maxsplit=1)
        pattern = list(map(list, pattern.split(sep="/"))) #ex: [['#', '.', '#'], ['#', '.', '.'], ['.', '.', '.']]
        output = list(map(list, output.split(sep="/"))) #ex: [['.', '.', '.', '#'], ['#', '.', '#', '#'], ['#', '#', '#', '#'], ['#', '#', '.', '#']]
        rules.update({i: {"pattern": pattern, "output": output}})
    return rules

#do a crude hash on counts of "#" per row of a given pattern
#for quicker pattern matching
def getRulesHash(rules):
    rulesHash = dict()
    for i, rule in rules.items():
        patternHash = [row.count("#") for row in rule["pattern"]]
        patternHash = "".join(map(str, patternHash))
        if patternHash not in rulesHash:
            rulesHash.update({patternHash: [i]})
        else:
            rulesHash[patternHash].append(i)
    return rulesHash

def doEnhancement(rules, iterations=1):
    rulesHash = getRulesHash(rules)
    pattern = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]] #initial pattern
    def hFlip(square):
        for row in square:
            row = row.reverse()
        return square
    def rotate(square):
        copy = [[x for x in row] for row in square]
        #transpose
        for row in range(len(square)):
            for col in range(len(square)):
                square[row][col] = copy[col][row]
        #flip
        hFlip(square)
        return square
    #apply enhancement rule for iteration times
    for _ in range(iterations):
        #determine size of the pattern (given by its length or width)
        #determine whether to break pattern into 3x3 or 2x2 smaller squares
        size = len(pattern)
        if size % 2 == 0:
            sqSize = 2
        elif size % 3 == 0:
            sqSize = 3
        quotient = int(size/sqSize)
        #break pattern into sqSize x sqSize squares
        #the squares are ordered left to right, top to down
        squares = list()
        for i in range(quotient): #for i rows of height == sqSize
            for j in range(quotient): #for j columns of width == sqSize
                colStart, colEnd = j*sqSize, (j+1)*sqSize
                if sqSize == 3:
                    row1, row2, row3 = [n + 3*i for n in range(3)]
                    square = [pattern[row1][colStart:colEnd], pattern[row2][colStart:colEnd], pattern[row3][colStart:colEnd]]
                elif sqSize == 2:
                    row1, row2 = [n + 2*i for n in range(2)]
                    square = [pattern[row1][colStart:colEnd], pattern[row2][colStart:colEnd]]
                squares.append(square)
        #find matching patterns, collect outputs
        outputs = list()
        for square in squares:
            rowHash = [row.count("#") for row in square]
            rowHash = "".join(map(str, rowHash))
            colHash = [row.count("#") for row in rotate(square)]
            colHash = "".join(map(str, colHash))
            #collect indices of patterns that might match square
            indices = list()
            for h in [rowHash, colHash, rowHash[::-1], colHash[::-1]]:
                try:
                    indices.extend(rulesHash[h])
                except KeyError:
                    pass
            #match square to patterns
            match = False
            for i in indices:
                #try matching four rotations of square
                #then try matching four rotations of flipped square
                for _ in range(8):
                    if rotate(square) == rules[i]["pattern"]:
                        outputs.append(rules[i]["output"])
                        match = True
                        break
                    if _ == 3:
                        hFlip(square)  
                if match:
                    break
        #form new pattern from collected outputs
        pattern.clear()
        for i in range(quotient):
            rows = [[],[],[],[]] #largest output is 4x4
            for output in outputs[i*(quotient):(i+1)*(quotient)]:
                rows = [rows[j] + output[j] for j in range(len(output))]
            pattern.extend(rows)
    return pattern

if __name__ == "__main__":
    main()