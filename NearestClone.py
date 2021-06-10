#!/bin/python3

import math
import os
import random
import re
import sys

def dfsrec(adj,s,visited,count):
        count += 1
        visited[s] = 1
        if ids[s-1]==val:
            return count
        else:
            temp = -1
            for u in adj[s]:
                if visited[u]==0:
                    temp = dfsrec(adj,u,visited,count)

            return temp
        
def findShortest(graph_nodes, graph_from, graph_to, ids, val):

    adj = dict()
    for i in range(len(graph_from)):
        if graph_from[i] in adj:
            adj[graph_from[i]].append(graph_to[i])
        else:
            adj[graph_from[i]] = [graph_to[i]]

        if graph_to[i] in adj:
            adj[graph_to[i]].append(graph_from[i])
        else:
            adj[graph_to[i]] = [graph_from[i]]




    f = 0
    for i in range(len(ids)):
        if ids[i]==val:
            f = 1
            for adjacent in adj[i+1]:
                if ids[adjacent-1]==val:
                    return 1

            l = []
            visited = [0]*(graph_nodes+1)
            visited[i+1] = 1
            for adjacent in adj[i+1]:
                variable = 0
                count = dfsrec(adj,adjacent,visited,variable)
                l.append(count)

            minn = 999999
            flag = 0
            for i in l:
                if i!=-1 and i<minn:
                    flag = 1
                    minn = i

            if flag==1:
                return minn
            else:
                return -1
        
    if  f==0:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
