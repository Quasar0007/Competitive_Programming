#User function Template for python3

class Solution:
    def antiDiagonalPattern(self,matrix):
        m = []
        for k in range(2*(len(matrix[0])-1)+1):
            m.append([])
        for i in range(len(matrix[0])):
            for j in range(len(matrix[0])):
                m[i+j].append(matrix[i][j])
        
        ans = []
        for i in range(len(m)):
            ans.extend(m[i])
        return ans
            
                
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        inp=list(map(int,input().split()))
        matrix=[]
        k = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(inp[k])
                k += 1
            matrix.append(row)
        ob = Solution()
        ans = ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends