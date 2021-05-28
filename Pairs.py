#!/bin/python3

import math
import os
import random
import re
import sys

def pairs(k, arr):
    arr.sort()
    i,j = 0,1
    res=0
    while i<len(arr) and j<len(arr):
        if k==arr[j]-arr[i]:
            i+=1
            j+=1
            res+=1
        elif k < arr[j]-arr[i]:
            i+=1
            if i==j:
                j+=1
        else:
            j+=1
                
    return res
            
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
