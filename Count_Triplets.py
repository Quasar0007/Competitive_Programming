#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    d_left={}
    d_right={}
    for i in range(len(arr)):
        if arr[i] not in d_right.keys():
            d_right[arr[i]]=1
        else:
            d_right[arr[i]]+=1
    total=0
    for i in range(len(arr)):
        d_right[arr[i]]-=1
        if arr[i]%r==0:
            total+=d_left.get(arr[i]//r,0)*d_right.get(arr[i]*r,0)
        if arr[i] in d_left.keys():
            d_left[arr[i]]+=1
        else:
            d_left[arr[i]]=1
    return total
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
