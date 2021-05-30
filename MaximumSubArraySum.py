#!/bin/python3

import math
import os
import random
import re
import sys

from bisect import bisect,insort

def maximumSum(a, m):
    cumulative_sums = []
    sum_so_far = 0
    max_sum = 0
    
    for i in range(len(a)):
        sum_so_far = (sum_so_far + a[i]) % m       
        pos = bisect(cumulative_sums, sum_so_far) 
        # Returns the position of the newly inserted list
        d = 0 if pos == i else cumulative_sums[pos]
        max_sum = max(max_sum, (sum_so_far + m - d) % m)
        insort(cumulative_sums, sum_so_far)
        # Insort return the list after the sorting. The bisect and insort operation takes O(logn) TC as they work on the principle of binary search
    
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
