#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(l):
    d={}
    for i in range(len(l)):
        d[l[i]]=l[i]-i-1
    for i in range(len(l)):
        if d[i+1]>2:
            print("Too chaotic")
            return
    swap=0
    for j in range(len(l)-1,1,-1):
        if l[j-1]==j+1:
            l[j],l[j-1]=l[j-1],l[j]
            swap+=1
        elif l[j-2]==j+1:
            l[j-2],l[j-1],l[j]=l[j-1],l[j],l[j-2]
            swap+=2
    if l[1]<l[0]:
        swap+=1
    print(swap)
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
