#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    d={}
    for letter in s:
        if letter in d.keys():
            d[letter]+=1
        else:
            d[letter]=1
    l=list(d.values())
    x1=l.count(l[0])
    x2=l.count(l[0]-1)
    x3=l.count(l[0]+1)
    if x1>=len(l)-1:
        return "YES"
    elif x2==len(l)-1 and x1==1:
        return "YES"
    else:
        return "NO"
            
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
