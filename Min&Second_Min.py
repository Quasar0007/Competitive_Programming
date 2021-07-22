def minAnd2ndMin( a, n):
    l=[]
    c=min(a)
    if n==1 or a==[c]*n:
        return [-1]
    for i in range(n):
        if a[i]==c:
            a[i] = 100001
    l.append(c)
    l.append(min(a))
    return l