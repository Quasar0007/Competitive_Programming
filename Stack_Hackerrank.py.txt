*****You have an empty sequence, and you will be given N queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.

==>k=[0]
a=[0]
for i in range(int(input())):
    l=[]
    l.extend(list(map(int,input().split())))
    if len(l)==2:
        k.append(l[1])
        top=k[-1]
        a.append(max(a[-1],top))
    elif l[0]==2:
        del(a[-1])
        del(k[-1])
        top=k[-1]
    else:
        print(a[-1])


#LOGIC:-Create a stack containing the top values as well and another stack containing the maximum values only and then perform according to the queries.
    


    
