# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    ar=[[0]]*(len(s1)+1)
    ar2=[0]*(len(s2))
    for i in range(len(s1)+1):
        ar[i]=ar[i]+ar2
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                ar[i+1][j+1]=ar[i][j]+1
            else:
                ar[i+1][j+1]=max(ar[i][j+1],ar[i+1][j])
    return ar[-1][-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
