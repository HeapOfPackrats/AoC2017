#http://adventofcode.com/2017/day/10

#see url at top for full specifications
#important instructions pasted at end of file

def main():
    with open("input10.txt") as inputFile:
        sequence = list(range(0, 256))
        lengths = map(lambda x: int(x), inputFile.read().split(sep=","))
        knotHash(sequence, lengths)
    print("The product of the first two elements after hashing is {}".format(sequence[0]*sequence[1]))

#in-place hashing of sequence
def knotHash(sequence, lengths):
    seqSize = len(sequence)
    currPos = 0
    skipSize = 0
    for length in lengths:
        if length > seqSize:
            print("Invalid length (length > size of sequence)")
            return
        if currPos+length > seqSize:
            remainder = (currPos+length)%(seqSize)
            subSeq = sequence[currPos:] 
            subSeq += sequence[:remainder]
            subSliceIndex = (remainder-1)
            sequence[currPos:] = subSeq[:subSliceIndex:-1]
            sequence[0:remainder] = subSeq[subSliceIndex::-1]
        else:
            subSeq = subSeq = sequence[currPos:currPos+length]
            sequence[currPos:currPos+length] = subSeq[::-1]
        currPos = (currPos + length + skipSize)%(seqSize)
        skipSize += 1

if __name__ == "__main__":
    main()

#"Begin with a (circular) list of numbers from 0 to 255, a current position which begins at 0 (the first element in the list),
#a skip size (which starts at 0), and a sequence of lengths (your puzzle input). Then, for each length:
#Reverse the order of that length of elements in the list, starting with the element at the current position.
#Move the current position forward by that length plus the skip size.
#Increase the skip size by one."