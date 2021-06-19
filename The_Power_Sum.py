#!/bin/python3

import math
import os
import random
import re
import sys

def powerSum(X, N):
    dp=[1]+[0]*X
    i=1
    while i**N <= X:
        u=i**N
        for j in range(X,u-1,-1):
            dp[j]+=dp[j-u]
        i+=1
    return dp[X]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
