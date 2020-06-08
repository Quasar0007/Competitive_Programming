*****David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball he has into its own container. David wants to sort the balls using his sort method.
As an example, David has n=2 containers and 2 different types of balls, both of which are numbered from 0 to n-1=1. The distribution of ball types per container are described by an n*n matrix of integers,M[container][type] . For example, consider the following diagram for M=[[1,4],[2,3]]:

In a single operation, David can swap two balls located in different containers.
The diagram below depicts a single swap operation:

David wants to perform some number of swap operations such that:

-Each container contains only balls of the same type.
-No two balls of the same type are located in different containers.
You must perform q queries where each query is in the form of a matrix,M. For each query, print Possible on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print Impossible.


==>for i in range(int(input())):
    n=int(input())
    l=[]
    for j in range(n):
        l.append(list(map(int,input().split())))
    k=(list(zip(*l)))
    for j in range(n):
        l[j]=sum(l[j])
        k[j]=sum(k[j])
    m=0
    while m<len(l):
        if l[m] in k:
            m+=1
        else:
            break
    if m==len(l):
        print("Possible")
    else:
        print("Impossible")


LOGIC:-The sum of no.of balls in a container should be equal to the no.of balls of a particular type.



