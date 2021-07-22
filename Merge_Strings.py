class Solution:
    def merge(self, S1, S2):
        if S1=="":
            return S2
        elif S2=="":
            return S1
        else:
            ans=""
            for i in range(min(len(S1), len(S2))):
                ans+=S1[i]+S2[i]
            ans+=S1[(i+1):]+S2[(i+1):]
            return ans