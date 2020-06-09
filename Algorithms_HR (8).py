# You have a string of lowercase English alphabetic letters. You can perform two types of operations on the string:
# Append a lowercase English alphabetic letter to the end of the string.
# Delete the last character in the string. Performing this operation on an empty string results in an empty string.
# Given an integer,k, and two strings,s and t, determine whether or not you can convert s to t by performing exactly k of the above operations on s. If it's possible, print Yes. Otherwise, print No.
# For example, strings s=[a,b,c] and t=[d,e,f]. Our number of moves,k=6 . To convert s to t, we first delete all of the characters in 3 moves. Next we add each of the characters of t in order. On the 6-th move, you will have the matching string. If there had been more moves available, they could have been eliminated by performing multiple deletions on an empty string. If there were fewer than 6 moves, we would not have succeeded in creating the new string.


s=input()
t=input()
n=int(input())
i=0
while i<len(t) and i<len(s):
    if s[i]==t[i]:
        i+=1
    else:
        break
if i<len(t) and i<len(s):
    d=len(s)-i+len(t)-i
elif i==len(t):
    d=len(s)-i
else:
    d=len(t)-i
if len(s)+len(t)<=n:
    print("Yes") 
elif s==t and 2*len(s)<=n:
    print("Yes")
elif n>=d and (n-d)%2==0:
    print("Yes")
else:
    print("No")


# LOGIC:-Cases could be when both strings are same or none of the letters of the string at the same position match or letters match to some extent only. 