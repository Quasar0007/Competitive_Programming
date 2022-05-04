#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        d={}
        for i in A:
            d[i]=1
        
        ans=[]
        s={}
        for i in B:
            if i in d.keys():
                d[i]=0
            else:
                s[i]=1
        
        for i in d.keys():
            if d[i]==1:
                ans.append(i)
        
        for i in s.keys():
            ans.append(i)
        
        if ans == []:
            return -1
        ans.sort()
        return ''.join(ans)
                
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends