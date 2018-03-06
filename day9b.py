#http://adventofcode.com/2017/day/9

#see url at top for full specifications
#findScore explains the logic briefly
def main():
    with open("input9.txt") as inputFile:
        print("The score is {}, and there are {} garbage characters".format(*findScoreAndCountGarbage(inputFile)))

#calculates score of groups (see url) and counts all non-"!", non-cancelled chars in garbage
def findScoreAndCountGarbage(inputFile):
    score = 0
    garbageCount = 0
    groupDepth = 0
    inGarbage = False
    chars = inputFile.read()
    charsIter = iter(chars)
    for char in charsIter:
        if char == "!": #if "!" skip/cancel the following character
            next(charsIter, None)
            continue
        elif inGarbage:
            if char == ">": #stop ignoring all non-"!" chars
                inGarbage = False
            else:
                garbageCount += 1 #count up all garbage chars that aren't cancelled or aren't "!" ">"
        else:
            if char == "{":
                groupDepth += 1 #enter a group. Subgroups are worth parent+1 in points
            elif groupDepth >= 1 and char == "}":
                score += groupDepth #add points for every group closed
                groupDepth -= 1
            elif char == "<": #ignore all non-"!" or non-">" chars (treat as garbage)
                inGarbage = True
    return score, garbageCount

if __name__ == "__main__":
    main()