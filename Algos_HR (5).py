# Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in S' is not evenly divisible by k.
# For example, the array S=[19,10,12,10,24,25,22] and k=4. One of the arrays that can be created is S'[0]=[10,12,25]. Another is S'[1]=[19,22,24]. After testing all permutations, the maximum length solution array has 3 elements.


n,k=map(int,input().split())
l=list(map(int,input().split()))
if k==1:
    print(1)
else:
    l=list(set(l))
    for i in range(len(l)):
        l[i]=l[i]%k
    c=list(set(l))
    m=[]
    count=0
    for i in range(len(c)):
        if c[i]==0 or c[i]==(k-c[i]):
            count+=1
        elif l.count(c[i])>l.count(k-c[i]):
            count+=l.count(c[i])
        elif l.count(c[i])==l.count(k-c[i]):
            count+=l.count(c[i])
            l.remove(k-c[i])
    print(count)



# LOGIC:-The remainder of each number after dividing by k is noted and the condition for the subset would be that the number and k-(that number) can't be in the same subset.
            

