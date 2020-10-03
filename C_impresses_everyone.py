import sys
def bsearch(a,ar,low,high):
    x=(low+high)//2
    if x==0 and ar[x]>a:
        return 0
    elif ar[x]==a:
        return x
    elif ar[x]<a and ar[x+1]>=a:
        return x+1
    elif ar[x]<a:
        return bsearch(a,ar,x,high)
    elif ar[x]>a and ar[x-1]<a:
        return x
    else:
        return bsearch(a,ar,low,x)

    

data = list(map(int, sys.stdin.readline().strip().split()))
n = data[0]
l = data[1:n + 1]
q = data[n + 1]
for i in range(n-1):
    l[i+1]+=l[i]
for j in range(q):
    pos=data[n+2+j]
    i=bsearch(l[-1]-pos+1,l,0,n-1)
    sys.stdout.write('A\n' if i % 2 ==0 else 'B\n')