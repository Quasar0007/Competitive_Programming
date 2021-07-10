import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap=[]
        heapq.heapify(heap)
        for i,sc in enumerate(score):
            heapq.heappush(heap, (-sc,i))
        n=len(score)
        l=[0]*n
        stack=["Gold Medal","Silver Medal", "Bronze Medal"]
        i=4
        while (n-3)>0:
            stack.append(str(i))
            i+=1
            n-=1
        while heap:
            sc,i = heapq.heappop(heap)
            l[i] = stack.pop(0)
        return l