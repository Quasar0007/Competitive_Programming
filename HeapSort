import heapq
#User function Template for python3

class Solution:

    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        new_ar = []
        for i in range(n):
            new_ar.append(arr[i])
        heapq.heapify(new_ar)
        for _ in range(n):
            arr.append(heapq.heappop(new_ar))
        del(arr[:n])
