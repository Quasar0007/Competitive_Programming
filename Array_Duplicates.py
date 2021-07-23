class Solution:
    def duplicates(self, arr, n): 
        d={}
        m=[]
        for i in arr:
            if i in d.keys():
                if d[i]==1:
                    m.append(i)
                d[i]+=1
            else:
                d[i]=1
        if m==[]:
            return [-1]
        m.sort()
        return m