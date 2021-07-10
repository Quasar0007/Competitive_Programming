class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, A):
        ans=[]
        if len(A)==1:
            return [A]

        for i in range(len(A)):
            temp=A[0]
            A[0]=A[i]
            A[i]=temp
            nxt=self.permute(A[1:])
            for j in nxt:
                ans.append([A[0]]+j)
        return ans
