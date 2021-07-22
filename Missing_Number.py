class Solution:
    def MissingNumber(self,array,n):
        d={}
        for i in range(n-1):
            d[array[i]]=1
        for i in range(1,n+1):
            if i not in d:
                return i
            