#input: number of cases, number of pets per case, sizes of pets
#output: minimum number of treats needed to feed each pet, and that pets of larger sizes get more treats than smaller ones
#find out how many different sizes there are, and how many pets of each size, then calculate sum

#dictionary with key as weight and the attached value being the # of pets of that weight
import sys
from sys import stdin,stdout

def get_ints(): 
    return list(map(int, sys.stdin.readline().strip().split()))

cases=int(stdin.readline())

for i in range(1,cases+1):
    petNum=stdin.readline()
    weights = get_ints()

    weights.sort()

    weight_and_qty=dict()

    for x in weights:
        if x in weight_and_qty:
            weight_and_qty[x] = weight_and_qty[x]+1
        else:
            weight_and_qty[x] = 1

    #total sum of minimum treats
    treats = 0
    #increases by weight category
    multiplier = 1

    for y in weight_and_qty:
        treats += weight_and_qty[y] * multiplier
        multiplier += 1
    print(" Case #"+str(i)+": "+str(treats))


