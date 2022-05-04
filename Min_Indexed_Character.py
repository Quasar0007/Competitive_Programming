#User function Template for python3

class Solution:
    
    def minIndexChar(self,Str, pat): 
        d = {}
        l=[]
        for i in range(len(Str)):
            if Str[i] not in d.keys():
                d[Str[i]]=i
        ans = 100000
        for i in pat:
            if i in d.keys():
                ans = min(ans,d[i])
        if ans == 100000:
            return -1
        return ans
            
            
            
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        obj = Solution()
        ans = obj.minIndexChar(s,p)
        print(ans)
# } Driver Code Ends