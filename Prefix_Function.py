def PrefixFunction(s):
	prefix_array=[0]*len(s)
	border=0
	for i in range(1,len(s)):
		while border>0 and (s[i]!=s[border]):
			border = prefix_array[border-1]
		if s[i]==s[border]:
			border+=1
		else:
			border=0
		prefix_array[i]=border
	return prefix_array