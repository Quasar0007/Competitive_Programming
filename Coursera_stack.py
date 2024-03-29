# A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
# Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().
# A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].
# By this logic, we say a sequence of brackets is balanced if the following conditions are met:
# It contains no unmatched brackets.
# The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
# Given n strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.


def is_match(left,right)
    return left+right in ("{}","[]","()")
for i in range(int(input())):
    l=[]
    a=input()
    for i in a:
        if (i is "{") or (i is "[") or (i is "("):
            l.append(i)
        elif l!=[] and is_match(l[-1],i):
            del(l[-1])
        else:
            print("NO")
            l.append(i)
            break
    if l==[]:
        print("YES")
    else:
        if l[-1] in ("(","{","["):
            print("NO")




# LOGIC:-Create a function is_match which returns true if the brackets match,now add the opening brackets in the list and use stack concept as the bracket first opened is closed first and is similar to the LIFO(Last-In First Out) concept of stacks.