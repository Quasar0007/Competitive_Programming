#User function Template for python3

class Solution:
    def solveQueries(self, n, Queries):
        output = []
        for i in range(n+1):
            l=[]
            for j in range(n+1):
                l.append(0)
            output.append(l)
    
    
        for query in Queries:
            for i in range(query[0], query[2]+1):
                output[i][query[1]]+=1
                output[i][query[3]+1]-=1
                
        for i in range(n):
            for j in range(1,n):
                output[i][j] += output[i][j-1]
            del(output[i][-1])
        del(output[-1])
        return output

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, q= input().split()
        n = int(n); q = int(q);
        Queries = [];
        for _ in range(q):
            cur = list(map(int, input().split()))
            Queries.append(cur);
        obj = Solution()
        ans = obj.solveQueries(n, Queries)
        for _ in ans:
            for __ in _:
                print(__, end = " ")
            print()

# } Driver Code Ends