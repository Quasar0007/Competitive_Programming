class Solution:
    def majorityElement(self, A, N):
        if N==1:
            return A[0]
        d={}
        for i in A:
            if i in d.keys():
                d[i]+=1
                if d[i]>N//2:
                    return i
            else:
                d[i]=1
        return -1