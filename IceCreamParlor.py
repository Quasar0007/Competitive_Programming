#!/bin/python3

import math
import os
import random
import re
import sys
def whatFlavors(cost, money):
    x=sorted(cost)
    i=0
    j=len(cost)-1
    while i<j :
        if x[i]+x[j] == money:
            break
        elif x[i]+x[j] > money:
            j-=1
        else:
            i+=1
    ind_1 = cost.index(x[i])
    cost[cost.index(x[i])]= float("inf")
    ind_2 = cost.index(x[j])
    if ind_1 <= ind_2:
        print(ind_1+1, ind_2+1)
    else:
        print(ind_2+1, ind_1+1)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
