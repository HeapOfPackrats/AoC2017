#http://adventofcode.com/2017/day/10

#see url at top for full specifications
#important instructions pasted at end of file

from operator import xor

def main():
    with open("input10.txt") as inputFile:
        sequence = list(range(0, 256))
        lengths = list(map(lambda c: ord(c), inputFile.read())) #convert all chars to ASCII code
        lengths += [17, 31, 73, 47, 23] #append sequence specified by specs
        print("The (dense) hex knot hash is {}".format(seqToHexStr(denseHash(sequence, lengths))))

#perform dense hash on sequence, return dense hash
def denseHash(sequence, lengths):
    #sparse hash
    seqSize = len(sequence)
    currPos = 0
    skipSize = 0
    for i in range(64):
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
    #condense sparse hash to dense hash
    denseHash = list()
    for i in range(16):
        denseVal = 0
        for n in sequence[(16*i):(16*(i+1))]:
            denseVal = xor(denseVal, n)
        denseHash.append(denseVal)
    return denseHash

#turn a seq of numbers into a single string with hex values (sans '0x', w/leading 0) concatenated
def seqToHexStr(sequence):
    hexStr = ""
    for val in sequence:
        hexStr += "{:02x}".format(val) #https://stackoverflow.com/a/33986725
    return hexStr

if __name__ == "__main__":
    main()

#"Begin with a (circular) list of numbers from 0 to 255, a current position which begins at 0 (the first element in the list),
#a skip size (which starts at 0), and a sequence of lengths (your puzzle input). Then, for each length:
#Reverse the order of that length of elements in the list, starting with the element at the current position.
#Move the current position forward by that length plus the skip size.
#Increase the skip size by one."

# The logic you've constructed forms a single round of the Knot Hash algorithm; running the full thing requires many of these rounds. Some input and output processing is also required.
# First, from now on, your input should be taken not as a list of numbers, but as a string of bytes instead. Unless otherwise specified, convert characters to bytes using their ASCII codes. This will allow you to handle arbitrary ASCII strings, and it also ensures that your input lengths are never larger than 255. For example, if you are given 1,2,3, you should convert it to the ASCII codes for each character: 49,44,50,44,51.
# Once you have determined the sequence of lengths to use, add the following lengths to the end of the sequence: 17, 31, 73, 47, 23. For example, if you are given 1,2,3, your final sequence of lengths should be 49,44,50,44,51,17,31,73,47,23 (the ASCII codes from the input string combined with the standard length suffix values).
# Second, instead of merely running one round like you did above, run a total of 64 rounds, using the same length sequence in each round. The current position and skip size should be preserved between rounds. For example, if the previous example was your first round, you would start your second round with the same length sequence (3, 4, 1, 5, 17, 31, 73, 47, 23, now assuming they came from ASCII codes and include the suffix), but start with the previous round's current position (4) and skip size (4).
# Once the rounds are complete, you will be left with the numbers from 0 to 255 in some order, called the sparse hash. Your next task is to reduce these to a list of only 16 numbers called the dense hash. To do this, use numeric bitwise XOR to combine each consecutive block of 16 numbers in the sparse hash (there are 16 such blocks in a list of 256 numbers). So, the first element in the dense hash is the first sixteen elements of the sparse hash XOR'd together, the second element in the dense hash is the second sixteen elements of the sparse hash XOR'd together, etc.
# For example, if the first sixteen elements of your sparse hash are as shown below, and the XOR operator is ^, you would calculate the first output number like this:
# 65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22 = 64
# Perform this operation on each of the sixteen blocks of sixteen numbers in your sparse hash to determine the sixteen numbers in your dense hash.
# Finally, the standard way to represent a Knot Hash is as a single hexadecimal string; the final output is the dense hash in hexadecimal notation. Because each number in your dense hash will be between 0 and 255 (inclusive), always represent each number as two hexadecimal digits (including a leading zero as necessary). So, if your first three numbers are 64, 7, 255, they correspond to the hexadecimal numbers 40, 07, ff, and so the first six characters of the hash would be 4007ff. Because every Knot Hash is sixteen such numbers, the hexadecimal representation is always 32 hexadecimal digits (0-f) long.
# Here are some example hashes:
# The empty string becomes a2582a3a0e66e6e86e3812dcb672a272.
# AoC 2017 becomes 33efeb34ea91902bb2f59c9920caa6cd.
# 1,2,3 becomes 3efbe78a8d82f29979031a4aa0b16a9d.
# 1,2,4 becomes 63960835bcdc130f0b66d7ff4f6a5a8e.
# Treating your puzzle input as a string of ASCII characters, what is the Knot Hash of your puzzle input? Ignore any leading or trailing whitespace you might encounter.