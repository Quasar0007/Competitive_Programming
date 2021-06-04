#!/bin/python3

import math
import os
import random
import re
import sys

def maxSubsetSum(arr):
    if len(arr) == 1:
        return max(arr[0],0)
    l=[arr[0],max(arr[0],arr[1])]
    for i in range(2, len(arr)):
        l.append(max(l[i-2]+arr[i],l[i-1],arr[i]))
    return max(max(l),0)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
