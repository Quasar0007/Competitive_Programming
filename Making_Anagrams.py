#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    d={}
    l={}
    for s in a:
        if s in d.keys():
            d[s]+=1
        else:
            d[s]=1
    for s in b:
        if s in l.keys():
            l[s]+=1
        else:
            l[s]=1
    l1=list(d.keys())
    l2=list(l.keys())
    common=l1+l2
    common=set(common)
    count=0
    for i in common:
        if i in d.keys() and i in l.keys():
            count+=abs(d[i]-l[i])
        elif i in d.keys():
            count+=d[i]
        else:
            count+=l[i]
    return count
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
