def chef(arr,n,k):
	s=sum(arr)
	optimal = s//k
	l=[]
	while i<n:
		cook=0
		while cook<optimal and i<n:
			cook+=arr[i]
			i+=1
		l.append(cook)
	return max(l)
print(chef([5,10,30,20,15],5,3))

