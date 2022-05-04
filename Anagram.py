#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        d= {}
        for i in a:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        
        for i in b:
            if i in d.keys():
                d[i]-=1
                if d[i]<0:
                    return False
            else:
                return False
        return True
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends