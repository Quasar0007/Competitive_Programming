# Happy Ladybugs is a board game having the following properties:

# The board is represented by a string, b, of length n. The i-th character of the string,b[i] , denotes the i-th cell of the board.
# If b[i] is an underscore (i.e., _), it means the i-th cell of the board is empty.
# If b[i] is an uppercase English alphabetic letter (ascii[A-Z]), it means the i-th cell contains a ladybug of color b[i].
# String b will not contain any other characters.
# A ladybug is happy only when its left or right adjacent cell (i.e.,b[i+_1]) is occupied by another ladybug having the same color.
# In a single move, you can move a ladybug from its current position to any empty cell.
# Given the values of n and b for g games of Happy Ladybugs, determine if it's possible to make all the ladybugs happy. For each game, print YES on a new line if all the ladybugs can be made happy through some number of moves. Otherwise, print NO.


# As an example,b=[YYR_B_BR] . You can move the rightmost B and R to make b=[YYRRBB__] and all the ladybugs are happy.


for i in range(int(input())):
    a=int(input())
    s=list(input())
    if s==['_']:
        print("YES")
    elif len(s)==1 and '_' not in s:
        print("NO")
    elif "_" not in s:
        for j in range(a):
            if j==0:
                if s[0]!=s[1]:
                    print("NO")
                    break
            elif j==(a-1):
                if s[j-1]!=s[j]:
                    j=a-2
                    print("NO")
                    break
            elif s[j]!=s[j+1] and s[j]!=s[j-1]:
                print("NO")
                break
        if j==(a-1):
            print("YES")
                
    else:
        for j in range(a):
            if j==(a-1):
                if s.count(s[j])==1 and s[j]!="_":
                    j=a-2
                    break
            elif s.count(s[j])<=1 and s[j]!="_":
                break
        if j==(a-1):
            print("YES")
        else:
            print("NO")
            


# LOGIC:-There should be atleast one underscore and the count of all other elements should be greater than 1 or if there is no underscore;the given string should already be a happy ladybug.
