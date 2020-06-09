# You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.
# Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, then print the height. The removals must be performed in such a way as to maximize the height.
# Note: An empty stack is still a stack.

l=list(map(int,input().split()))
s1=list(map(int,input().split()))
s1.reverse()
s2=list(map(int,input().split()))
s2.reverse()
s3=list(map(int,input().split()))
s3.reverse()
h1=sum(s1)
h2=sum(s2)
h3=sum(s3)
m=max(h1,h2,h3)
while ((h1!=h3 or h2!=h3 or h1!=h2) and h1!=0 and h2!=0 and h3!=0):
    if m==h1:
        h1=h1-s1[-1]
        del(s1[-1])
        m=max(h1,h2,h3)
    elif m==h2:
        h2=h2-s2[-1]
        del(s2[-1])
        m=max(h1,h2,h3)
    else: 
        h3=h3-s3[-1]
        del(s3[-1])
        m=max(h1,h2,h3)
if h1==0 or h2==0 or h3==0:
    print(0)
else:
    print(m)


# LOGIC:-Look for the stack with maximum height and remove the top and continue doing it until all the 3 stacks are of the same size or one of them becomes 0.If one of them becomes 0,print 0.
