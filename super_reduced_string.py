# Steve has a string of lowercase characters in range ascii[‘a’..’z’]. He wants to reduce the string to its shortest length by doing a series of operations. In each operation he selects a pair of adjacent lowercase letters that match, and he deletes them. For instance, the string aab could be shortened to b in one operation.

# Steve’s task is to delete as many characters as possible using this method and print the resulting string. If the final string is empty, print Empty String.


ls=list(input())
i=0
while i<len(ls)-1:
    if ls[i+1]==ls[i]:
        del(ls[i])
        del(ls[i])
        if i!=0:
            i-=1
    else:
        i+=1
if ls!=[]:
    print(''.join(ls))
else:
    print("Empty String")