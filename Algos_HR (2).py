# Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.
# Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:
# It must be greater than the original word
# It must be the smallest word that meets the first condition
# For example, given the word w=abcd, the next largest word is abdc.
# Complete the function biggerIsGreater below to create and return the new string meeting the criteria. If it is not possible, return no answer.


for i in range(int(input())):
    s=list(input())
    k=sorted(s)
    k.reverse()
    if k==s:
        print("no answer")
    else:
        m=[s[-1]]
        for i in range(len(s)-2,-1,-1):
            if s[i+1]>s[i]:
                break
            else:
                m.append(s[i])
        a=s[i]
        m.sort()
        z=0
        while m[z]<=s[i]:
            z+=1
        s[i]=m[z]
        del(m[z])    
        m.append(a)
        s=s[:(i+1)]
        m.sort()
        print(''.join(s+m))

                



# LOGIC:-Check the string from the last until the previous element is not greater than the current one,when that loop breaks replace the current element with the smallest of all elements passed condition that the smallest element should be greater than the current one.Now sort all the passed elements and add it with the new element that replaced the current element.