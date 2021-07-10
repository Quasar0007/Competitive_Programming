import math
import os
import random
import re
import sys

def luckBalance(k, contests):
    l=[]
    luck=0
    for cont in contests:
        if cont[1]==1:
            l.append(cont[0])
        else:
            luck+=cont[0]
    l.sort(reverse= True)
    if k>= len(l):
        luck+=sum(l)
    else:
        x=sum(l)
        y=sum(l[0:k])
        luck+=(2*y-x)
    return luck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
