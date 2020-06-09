# Given an array of integers, determine whether the array can be sorted in ascending order using only one of the following operations one time.
# Swap two elements.
# Reverse one sub-segment.
# Determine whether one, both or neither of the operations will complete the task. If both work, choose swap. For instance, given an array [2,3,5,4] either swap the 4 and 5, or reverse them to sort the array. Choose swap. The Output Format section below details requirements.


n=int(input())
l=list(map(int,input().split()))
a=sorted(l)
if a==l:
    print("yes")
else:
    k=[]
    for i in range(n):
        if a[i]==l[i]:
            continue
        else:
            k.append(l[i])
    if len(k)==2:
        x=l.index(k[0])
        b=l.index(k[1])
        l[b]=k[0]
        l[x]=k[1]
        if a==l:
            print("yes")
            print("swap "+str(x+1)+" "+str(b+1))
        else:
            print("no")
    else:
        if (l.index(k[0])+l.index(k[-1]))%2==0:
            if l[(l.index(k[0])+l.index(k[-1]))//2]==a[(l.index(k[0])+l.index(k[-1]))//2]:
                k=k[:len(k)//2]+[l[(l.index(k[0])+l.index(k[-1]))//2]]+k[len(k)//2:]
        k.reverse()
        m=l.index(k[-1])
        for j in range(len(k)):
            l[m+j]=k[j]
        if a==l:
            print("yes")
            print("reverse "+str(m+1)+" "+str(m+len(k)))
        else:
            print("no")


# LOGIC:-Store all the elements in a list which aren't in their sorted position;if the number of elements not following the criteria is 2,check if the list can be sorted by swapping those 2 numbers;else check for the reversing.Special case is when a number is in its sorted position ,but is in between those numbers that aren't sorted should also be appended in the list containg the numbers that aren't in their correct position.
