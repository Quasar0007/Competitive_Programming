#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        s=[]
        for i in range(n):
            s.append(len(arr[i]))
        k = s.index(min(s))
        req_str = arr[k]
        ans = []
        for j in range(s[k]):
            for i in range(n):
                if arr[i][j]==req_str[j]:
                    res=1
                else:
                    res = 0
                    break
            if res == 1 :
                ans.append(arr[i][j])
        if ans!=[]:
            return ''.join(ans)
        else:
            return -1
        
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends