#http://adventofcode.com/2017/day/9

#see url at top for full specifications
#findScore explains the logic briefly
def main():
    with open("input9.txt") as inputFile:
        print("The score is {}".format(findScore(inputFile)))

def findScore(inputFile):
    score = 0
    groupDepth = 0
    inGarbage = False
    chars = inputFile.read()
    charsIter = iter(chars)
    for char in charsIter:
        if char == "!": #if "!" skip the following character
            next(charsIter, None)
            continue
        elif inGarbage:
            if char == ">": #stop ignoring all non-"!" chars
                inGarbage = False
        else:
            if char == "{":
                groupDepth += 1 #enter a group. Subgroups are worth parent+1 in points
            elif groupDepth >= 1 and char == "}":
                score += groupDepth #add points for every group closed
                groupDepth -= 1
            elif char == "<": #ignore all non-"!" or non-">" chars
                inGarbage = True
    return score

if __name__ == "__main__":
    main()