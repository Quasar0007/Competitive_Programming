import random
def partitioning(A,first_index,last_index):
    i=first_index
    for j in range(first_index,last_index):
        if A[last_index]>=A[j]:
            A[j],A[i]=A[i],A[j]
            i+=1
    A[i],A[last_index]=A[last_index],A[i]
    return i
def quick_sort(A,fi,li):
    if fi<li:
        s=partitioning(A,fi,li)
        quick_sort(A,fi,s-1)
        quick_sort(A,s+1,li)

A=random.sample(range(0,10),5)
print(A)
quick_sort(A,0,len(A)-1)
print(A)
