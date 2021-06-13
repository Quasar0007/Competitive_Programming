#!/bin/python3

import math
import os
import random
import re
import sys


def primality(n):
    if n==1:
        return "Not prime"
    elif n==2:
        return "Prime"
    elif n%2==0:
        return "Not prime"
    else:
        f=math.ceil(math.sqrt(n))
        for i in range(3,f+1,2):
            if n%i==0:
                return "Not prime"
            
        return "Prime"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input().strip())

    for p_itr in range(p):
        n = int(input().strip())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
