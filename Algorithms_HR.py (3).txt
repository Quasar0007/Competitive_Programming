*****Given a sequence of integers a, a triplet(a[i],a[j],a[k])  is beautiful if:
i<j<k
a[j]-a[i]=a[k]-a[j]=d

Given an increasing sequenc of integers and the value of d, count the number of beautiful triplets in the sequence.

For example, the sequence arr=[2,2,3,4,5] and d=1. There are three beautiful triplets, by index: [i,j,k]=[0,2,3],[1,2,3],[2,3,4] . To test the first triplet,arr[j]-arr[i]=3-2=1 and arr[k]-arr[j]=4-3=1.


==>n,d=map(int,input().split())
l=list(map(int,input().split()))
k=0
for i in range(n):
    if l[i]+d in l and l[i]+2*d in l:
        k+=1
print(k)


LOGIC:-As the list is in increasing sequence,we only need to check if the upcoming numbers are in the list or not.

                    
