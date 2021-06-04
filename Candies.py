#!/bin/python3

import math
import os
import random
import re
import sys

def candies(n, arr):
    candy=[1]*n
    for i in range(n-1):
        if arr[i+1]>arr[i]:
            candy[i+1]=candy[i]+1
    for j in range(n-1,0,-1):
        if arr[j-1]>arr[j] and candy[j-1]<=candy[j]:
            candy[j-1]=candy[j]+1
    return sum(candy)
            
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
