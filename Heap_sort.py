def max_heapify(A,i,size):
    l=2*i+1
    r=2*i+2
    largest=i
    if l<size and A[l]>A[i]:
        largest=l
    if r<size and A[r]>A[largest]:
        largest=r
    if largest!=i:
        A[i],A[largest]=A[largest],A[i]
        max_heapify(A,largest,size)

def build_heap(A):
    for j in range(len(A)//2,-1,-1):
        max_heapify(A,j,len(A))
def heapsort(A):
    build_heap(A)
    size=len(A)
    for i in range(len(A)-1):
        A[-(i+1)],A[0]=A[0],A[-(i+1)]
        size-=1
        max_heapify(A,0,size)
    return A
print(heapsort(list(map(int,input().split()))))



