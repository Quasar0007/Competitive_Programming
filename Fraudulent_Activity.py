#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    if len(expenditure)==d:
        return 0
    l=[0]*201
    for i in range(d-1):
        l[expenditure[i]]+=1
    notifications=0
    for i in range(d,len(expenditure)):
        l[expenditure[i-1]]+=1
        if d%2==0:
            freq1=d//2
            freq2=d//2+1
            j=0
            while freq1>0:
                freq1-=l[j]
                j+=1
            median1 = j-1
            j=0
            while freq2>0:
                freq2-=l[j]
                j+=1
            median2 = j-1
            median=(median1+median2)/2
                
        else:
            freq=d//2+1
            j=0
            while freq>0:
                freq-=l[j]
                j+=1
            median = j-1
        if expenditure[i]>= 2*median:
            notifications+=1
        l[expenditure[i-d]]-=1
    return notifications

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
