*****In this challenge, you must implement a simple text editor. Initially, your editor contains an empty string,S . You must perform Q operations of the following 4 types:

1.append(W) - Append string W to the end of S.
2.delete(k) - Delete the last k characters of S.
3.print(k) - Print the k-th character of S.
4.undo() - Undo the last (not previously undone) operation of type 1 or 2, reverting S to the state it was in prior to that operation.

==>s=""
k=[]
for i in range(int(input())):
    l=list(map(str,input().split()))
    if l[0]=="1":
        k.append(s)
        s+=l[1]
    elif l[0]=="2":
        k.append(s)
        s=s[:(len(s)-int(l[1]))]
    elif l[0]=="3":
        print(s[int(l[1])-1])
    else:
        s=k.pop()



LOGIC:-Store all the changes made in S in a list and pop out the last element when said to undo and follow the other steps as directed.