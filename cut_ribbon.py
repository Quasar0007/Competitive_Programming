# Polycarpus has a ribbon, its length is n. He wants to cut the ribbon in a way that fulfils the following two conditions:
# After the cutting each ribbon piece should have length a, b or c.
# After the cutting the number of ribbon pieces should be maximum.
# Help Polycarpus and find the number of ribbon pieces after the required cutting.

# Input
# The first line contains four space-separated integers n, a, b and c (1 ≤ n, a, b, c ≤ 4000) — the length of the original ribbon and the acceptable lengths of the ribbon pieces after the cutting, correspondingly. The numbers a, b and c can coincide.

# Output
# Print a single number — the maximum possible number of ribbon pieces. It is guaranteed that at least one correct ribbon cutting exists.

def max_rib(n):
    ribbon=[float("-inf")]*(n+1)
    ribbon[0]=0
    for i in range(1,n+1):
        for pieces in l:
            if i-pieces >= 0:
                ribbon[i]=max(ribbon[i],1+ribbon[i-pieces])
    return ribbon[n]
l=list(map(int,input().split()))
n,l=l[0],l[1:]
print(max_rib(n))