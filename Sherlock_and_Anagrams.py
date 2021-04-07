#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    l=[]
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            l.append(''.join(s[i:j]))
    for k in range(len(l)):
        l[k]=''.join(sorted(l[k]))
    count=Counter(l)
    
    total=0
    for value in count.values():
        total+= value*(value-1)//2
    return total
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        fptr.write(str(result) + '\n')
    fptr.close()
