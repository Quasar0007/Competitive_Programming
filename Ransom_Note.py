#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dm={}
    dn={}
    for i in note:
        if i in dn:
            dn[i]+=1
        else:
            dn[i]=1
    for i in magazine:
        if i in dm:
            dm[i]+=1
        else:
            dm[i]=1
    for key in dn:
        if key in dm:
            if dm[key]>=dn[key]:
                continue
            else:
                print("No")
                return
        else:
            print("No")
            return
    print("Yes")
    return
            

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
