# You are a waiter at a party. There are N stacked plates on pile Ao. Each plate has a number written on it. Then there will be Q iterations. In i-th iteration, you start picking up the plates in A(i-1) from the top one by one and check whether the number written on the plate is divisible by the i-th prime. If the number is divisible, you stack that plate on pile B(i). Otherwise, you stack that plate on pile A(i). After Q iterations, plates can only be on pile ,B1,B2,...,B(Q),A(Q) . Output numbers on these plates from top to bottom of each piles in order of B1,B2,....B(Q),A(Q).

l=[2,3,5]
for i in range(7,10000):
    j=2
    while j<(i//2):
        if i%j!=0:
            j+=1
        else:
            break
    if j==(i//2):
        l.append(i)
a,b=map(int,input().split())
c=list(map(int,input().split()))
for k in range(b):
    A=[]
    B=[]
    for e in c:
        if e%l[k]==0:
            B.append(e)
        else:
            A.append(e)
    A.reverse()
    B.reverse()
    c=A
    for m in range(len(B)):
        print(B[-1])
        del(B[-1])
for n in range(len(c)):
    print(c[-1])
    del(c[-1])


# LOGIC:-First ,write a code to get the i-th prime number ,then follow the conditions as given in the problem statement.
    





        













