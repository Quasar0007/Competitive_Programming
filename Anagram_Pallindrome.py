class Solution:

    def isPossible(self, S):
        new = list(set(list(S)))
        d={}
        for i in new:
            d[i]=0
        for i in S:
            d[i]+=1
        count=0
        for i in d.values():
            if i%2!=0:
                count+=1
        
        if (count<=1):
            return True
        else:
            return False