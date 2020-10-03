l = [1, 6, 31, 156, 781, 3906, 19531, 97656, 488281, 2441406, 12207031, 61035156, 305175781, 1525878906]
m = [5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625, 1220703125, 6103515625]
for j in range(int(input())):
	n = int(input())
	if n in l:
		expected_pow = 1 + l.index(n)
		print(pow(5, expected_pow))
	else:
		for i in range(13):
			if l[i]<n<l[i+1]:
				lp=i
				break
		soln=0
		while n>0:
			exp,n=divmod(n,l[lp])
			soln+=exp*m[lp]
			lp-=1
		print(soln)







