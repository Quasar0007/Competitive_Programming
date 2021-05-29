#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a=set(a)
    a=list(a)
    a.sort()
    c=set(c)
    c=list(c)
    c.sort()
    b=set(b)
    b=list(b)
    b.sort()
    i=0
    k=0
    res=0
    for j in range(len(b)):
        while i<len(a):
            if a[i]<=b[j]:
                i+=1
            else:
                break
        while k<len(c):
            if c[k]<=b[j]:
                k+=1
            else:
                break
        res+=i*k
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
