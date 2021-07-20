class Solution:
    def bs(self,ar,left,right ):
        if right-left==3:
            if ar[left]!=ar[left+1]:
                return ar[left]
            else:
                return ar[left+2]
        mid = (left+right)//2
        if mid%2==0:
            if ar[mid]==ar[mid+1]:
                return self.bs(ar,mid,right)
            elif ar[mid]==ar[mid-1]:
                return self.bs(ar,left,mid+1)
            else:
                return ar[mid]
        else:
            if ar[mid]==ar[mid-1]:
                return self.bs(ar,mid+1,right)
            elif ar[mid]==ar[mid+1]:
                return self.bs(ar,left,mid)
            else:
                return ar[mid]
            
    def findOnce(self,arr : list, n : int):
        if n==1:
            return arr[0]
        else:
            return self.bs(arr,0,n)