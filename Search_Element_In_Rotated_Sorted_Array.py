def pivot_index(arr,first,last):
    mid = (first+last)//2
    if arr[mid]>arr[last]:
        if last-first==2:
            return mid
        else:
            return pivot_index(arr,mid,last)
    elif arr[mid]<arr[first]:
        if mid-first==1:
            return first
        else:
            return pivot_index(arr,first,mid)
    else:
        return last
def bin_search(arr,first,last,k):
    if last<first:
        return -1
    if last==first and arr[last]!=k:
        return -1
    mid=(last+first)//2
    if arr[mid]==k:
        return mid
    elif arr[mid]>k:
        return bin_search(arr,first,mid-1,k)
    else:
        return bin_search(arr,mid+1,last,k)
        

def Search(arr,n,k):
    if n==1:
        if arr[0]==k:
            return 0
        else:
            return -1
    elif n==2:
        if arr[0]==k:
            return 0
        elif arr[1]==k:
            return 1
        else:
            return -1
    else:
        p=pivot_index(arr,0,n-1)
        if k==arr[p]:
            return p
        elif k>arr[p]:
            return -1
        else:
            if k>=arr[0]:
                return bin_search(arr,0,p-1,k)
            else:
                return bin_search(arr,p+1,n-1,k)
                