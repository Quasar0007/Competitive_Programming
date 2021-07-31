class Solution:  
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        if n==1:
            return a[0]
        elif n==2:
            return max(a[0],a[1])
        else:
            excl_prev = a[0]
            # incl_prev= max(a[0],a[1])
            excl_cur = max(a[0],a[1])
            incl_cur = excl_prev+a[2]
            for i in range(3,n):
                excl_prev = excl_cur
                # incl_prev = incl_cur
                excl_cur = max(incl_cur,excl_prev)
                incl_cur = max(excl_prev+a[i],incl_cur)
            return incl_cur