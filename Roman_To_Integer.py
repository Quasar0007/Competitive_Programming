class Solution:
    def romanToInt(self, s: str) -> int:
        d={}
        d["I"]= [0,1]
        d["V"]= [1,5]
        d["X"]= [2,10]
        d["L"]= [3,50]
        d["C"]= [4,100]
        d["D"]= [5,500]
        d["M"]= [6,1000]
        sum_num=0
        i=0
        while i<(len(s)-1):
            if d[s[i]][0]<d[s[i+1]][0]:
                sum_num+=d[s[i+1]][1]-d[s[i]][1]
                i+=2
            else:
                sum_num+=d[s[i]][1]
                i+=1
        if i<len(s):
            if d[s[i]][0]<=d[s[i-1]][0]:
                sum_num+=d[s[i]][1]
        return sum_num