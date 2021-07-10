#You have been given an array A of size N . you need to sort this array non-decreasing oder using bubble sort. However, you do not need to print the sorted array . You just need to print the number of swaps required to sort this array using bubble sort

n=int(input())
l=list(map(int,input().split()))
swaps=0
for i in range(n-1):
    for j in range(n-1,i,-1):
        if l[j]<l[j-1]:
            l[j],l[j-1]=l[j-1],l[j]
            swaps+=1
print(swaps)
