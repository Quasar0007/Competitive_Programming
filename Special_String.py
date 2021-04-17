#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count=n
    i=n-1
    while i>-1:
        store=s[i]
        lc=1
        j=-1
        while (i+j)>-1:
            if s[i+j]==store:
                lc+=1
                j-=1
            else:
                break
        take=lc
        while (i+j-1)>-1 and lc>0:
            if s[i+j-1]==store:
                lc-=1
                j-=1
            else:
                break
        count+=take*(take-1)//2+(take-lc)
        i-=take
    return count
            
        
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
