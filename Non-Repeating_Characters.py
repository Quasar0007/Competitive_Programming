class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        d={}
        for i in s:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        for i in s:
            if d[i]==1:
                return i
        return '$'