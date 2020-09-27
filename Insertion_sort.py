# You have been given an A array consisting of N integers. All the elements in this array are guaranteed to be unique. For each position i in the array A you need to find the position A[i] should be present in, if the array was a sorted array. You need to find this for each i and print the resulting solution.

def insertion_sort(ar):
	if len(ar)==1 or len(ar)==0:
		return ar
	else:
		i=1
		while i<len(ar):
			j=i
			while j>0 and ar[j]<ar[j-1]:
				ar[j-1],ar[j]=ar[j],ar[j-1]
				j=j-1
			i+=1
		return ar
n=int(input())
ls=list(map(int,input().split()))
m={}
for i in range(n):
	m[i]=ls[i]
ls=insertion_sort(ls)
k=[]
for i in range(n):
	k.append(ls.index(m[i])+1)
print(*k)

