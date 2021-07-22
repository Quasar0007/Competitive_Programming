class Solution:
    def check(self,A,B,N):
        d={}
        e={}
        for i in range(len(A)):
            if A[i] in d.keys():
                d[A[i]]+=1
            else:
                d[A[i]]=1
        for i in range(len(B)):
            if B[i] in e.keys():
                e[B[i]]+=1
            else:
                e[B[i]]=1
        for x in d.keys():
            if x in e.keys():
                if d[x]==e[x]:
                    continue
                else:
                    return False
            else:
                return False
        return True