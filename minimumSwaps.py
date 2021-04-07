#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    i=0
    swaps=0
    while i<len(arr):
        if arr[i]==(i+1):
            i+=1
        else:
            j=arr[i]
            k=arr[arr[i]-1]
            l=arr[i]-1
            arr[i],arr[l]=k,j
            swaps+=1
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
