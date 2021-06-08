#!/bin/python3

import math
import os
import random
import re
import sys


def superDigit(n, k):
    s=0
    for i in n:
        s+=int(i)
    s=str(s*k)
    if len(s)<=1 :
        return s
    else:
        return superDigit(s,1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
