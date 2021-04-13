#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    l = []
    arr = dict()
    freq = defaultdict(int)

    for x in queries:
        nums, value  = x    
        initial = arr.get(value, 0)

        if nums == 3:            
                l.append(1 if freq.get(value) else 0)                    
        else:            
                freq[initial] -= 1            
                if nums == 1:
                        arr[value] = initial + 1
                elif nums == 2 and initial:
                        arr[value] -= 1

                freq[arr.get(value,0)] += 1           

    return l
            
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
