*****Alexa has two stacks of non-negative integers, stackA=[a0,a1,....a(n-1)]  and stackB=[b0,b1,....b(n-1)] where index 0 denotes the top of the stack. Alexa challenges Nick to play the following game:

In each move, Nick can remove one integer from the top of either stack A or stack B.
Nick keeps a running sum of the integers he removes from the two stacks.
Nick is disqualified from the game if, at any point, his running sum becomes greater than some integer x given at the beginning of the game.
Nick's final score is the total number of integers he has removed from the two stacks.
Given A, B, and x for g games, find the maximum possible score Nick can achieve (i.e., the maximum number of integers he can remove without being disqualified) during each game and print it on a new line.

==>for i in range(int(input())):
    l=list(map(int,input().split()))
    s1=list(map(int,input().split()))
    s2=list(map(int,input().split()))
    k=0
    i=1
    while i<(l[0]+1):
        a=sum(s1[:i])
        if a<=l[2]:
            i+=1
        else:
            break
    k=i-1
    m=s1[:k]
    m.reverse()
    m.extend(s2)
    for x in range(k):
        j=i-x
        while j<(i+l[1]-x):
            a=sum(m[:j])
            if a<=l[2] and j<=len(m):
                k=max(k,j)
                j+=1
            else:
                break
        del(m[0])
    b=1
    while b<(l[1]+1):
        a=sum(s2[:b])
        if a<=l[2]:
            b+=1
        else:
            break
    k=max(k,b-1)
    c=b-1
    d=s2[:c]
    d.reverse()
    d.extend(s1)
    for e in range(c):
        f=b-e
        while f<(b+l[1]-e):
            a=sum(d[:f])
            if a<=l[2] and f<=len(d):
                k=max(k,f)
                f+=1
            else:
                break
        del(d[0])
    print(k)


LOGIC:-We first need to check for the no.of integers counted in a particular stack to reach the sum and then take that sub-list out separately.Then,we add the next list in that sub-list with sub-list in the reverse order and start removing one element from the starting of the joint list and calculating the total no.of integers counted and take out the maximum of the two comparisons.We need to repeat the same procedure with the other given list and take the maximum integer count of all the cases formed so.