#Function to locate the occurrence of the string x in the string s.
def strstr(s,x):
    i=0
    while i < len(s):
        k=i
        for j in range(len(x)):
            if k<len(s):
                if s[k]==x[j]:
                    res = 1
                    k+=1
                    pass
                else:
                    res = 0
                    break
            else:
                res = 0
                break
        if res == 1:
            return i
            break
        else:
            i+=1
    return -1
    
#{ 
#  Driver Code Starts
#Contributed by : Nagendra Jha

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

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        s,p =input().strip().split()
        print(strstr(s,p))


# } Driver Code Ends