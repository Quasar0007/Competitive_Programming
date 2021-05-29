#!/bin/python3
import math
import os
import random
import re
import sys
def time_taken(bound, machines):
    res=0
    for i in range(len(machines)):
        res+= bound//machines[i]
    return res
    
def minTime(machines, goal):
    slowest=max(machines)
    fastest = min(machines)
    lower_bd= (fastest*goal)//len(machines)
    upper_bd = (slowest*goal)//len(machines)+1
    while lower_bd<upper_bd:
        bs=(upper_bd+lower_bd)//2
        les=time_taken(bs, machines)
        if les>=goal:
            upper_bd = bs
        else:
            lower_bd = bs + 1
    return lower_bd
          
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nGoal = input().split()
    n = int(nGoal[0])
    goal = int(nGoal[1])
    machines = list(map(int, input().rstrip().split()))
    ans = minTime(machines, goal)
    fptr.write(str(ans) + '\n')

    fptr.close()
