# You are given an array A of non-negative integers of size m. Your task is to sort the array in non-decreasing order and print out the original indices of the new sorted array.

# Example:

# A={4,5,3,7,1}

# After sorting the new array becomes A={1,3,4,5,7}.

# The required output should be "4 2 0 1 3"   


n=int(input())
l=list(map(int,input().split()))
l_sort=sorted(l)
p=[]
if l_sort==l:
    for i in range(n):
        p.append(i)
else:
    for i in range(n):
        s=l.index(l_sort[i])
        p.append(s)
        l[s]=-1
print(*p)