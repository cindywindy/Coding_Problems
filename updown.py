"""We want to build a string with English alphabet uppercase letters in sorted order. However, we want the order to be sometimes strictly increasing and sometimes strictly decreasing.

The first letter of the string must be A. After that, the string must contain one or more blocks of letters. The i-th block must contain exactly Li letters. Each letter in the i-th block must be later in the alphabet than its preceding letter in the string if i is odd and earlier in the alphabet than its preceding letter if i is even. Notice that for the first letter of a block, its preceding letter exists, even though it is not in the block. Strings that follow all of these rules are called valid. There can be multiple valid strings, and we want to find the alphabetically first one.

For example, if there are 2 blocks of sizes L1=2 and L2=3, the string must have exactly 1+L1+L2=1+2+3=6 letters (the 1 is for the initial A). The strings XYZYBA, AZYCBA and AYZYBB are not valid for this case because they violate the required starting letter condition, and the ordering conditions in the first and second block, respectively. The string AYZYBA is valid. The string ABDCBA is also valid and, moreover, it is the alphabetically first valid string.

Given the sizes of the blocks, output the valid string that comes first in alphabetical order in the list of all valid strings. It can be shown that, for all inputs within the given limits, at least one valid string exists.

[incomplete]
"""
import sys
from sys import stdin,stdout
import string

alphy = list(string.ascii_uppercase)
print (alphy)


def get_ints(): 
    return list(map(int, sys.stdin.readline().strip().split()))

cases=int(stdin.readline())

for i in range(1,cases+1):
    blockQty=int(stdin.readline())
    block_sizes = get_ints()
    stringy='A'
    for x in range(1,blockQty+1):
        if (x%2 == 1) :
            print("odd block")
            if ((block_sizes[x-1] > block_sizes[x]) or (block_sizes[x-1] == block_sizes[x])):
                for y in range (0,block_sizes[x-1]):
                    index = alphy.index(stringy[-1])
                    stringy = stringy + alphy[index+1]
                    print(stringy)
            else:
                for y in range (0,block_sizes[x-1]-1):
                    index = alphy.index(stringy[-1])
                    stringy = stringy + alphy[index+1]
                    print(stringy)
                stringy = stringy + alphy[block_sizes[x]]
                print(stringy)
        else:
            print("even block")
            index = block_sizes[x-1] - 1
            for z in range (0,block_sizes[x-1]):
                stringy = stringy + alphy[index]
                index -= 1
                print (stringy)

