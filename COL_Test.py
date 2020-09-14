# Fill up an array of size N in increasing order with rst N of all numbers
# divisible by no primes other than 2, 3 and 5.
def prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(1,n//2+1):
            if n%(i)==0 and i!=1:
                return False
    return True

    
def check(n):
    if n==2 or n==3 or n==5:
        return True
    else:
        for i in range(1,n+1):
            if n%i==0:
                if prime(i) and (i!=2 and i!=3 and i!=5):
                    return False
        return True

def ar(N):
    if N==1:
        return [1]
    elif N==2:
        return [1,2]
    else:
        i=1
        while not check(ar(N-1)[-1]+i):
            i+=1
        s=ar(N-1)
        s.append(s[-1]+i)
        return s
n=int(input())
print(ar(n))
