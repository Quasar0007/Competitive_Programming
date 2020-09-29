You are given an array of n integer numbers a1, a2, .. ,an. Calculate the number of pair of indices (i,j) such that 1<=i<j<=n and ai xor aj = 0.

n=int(input())
l=list(map(int,input().split()))
d={}
for _ in l:
    d[_]=0
for i in l:
    d[i]+=1
ct=0
for i in d.values():
    ct+=i*(i-1)//2
print(ct)