class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        l=[0]*n
        if n==1:
            return ["Gold Medal"]
        elif n==2:
            if score[0]>score[1]:
                return ["Gold Medal","Silver Medal"]
            else:
                return ["Silver Medal", "Gold Medal"]
        else:
            stack=["Gold Medal","Silver Medal", "Bronze Medal"]
            i=4
            while (n-3)>0:
                stack.append(str(i))
                i+=1
                n-=1
            for _ in range(len(score)):
                x=score.index(max(score))
                l[x]=stack.pop(0)
                score[x]=-1
            return l
                
                
                
                
            
        