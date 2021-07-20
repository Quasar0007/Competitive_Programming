class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        count=0
        one=0
        res=False
        for i in d.keys():
            if d[i]%2==0:
                count+=d[i]
            else:
                res=True
                count+=d[i]-1
        if res:
            return count+1
        else:
            return count