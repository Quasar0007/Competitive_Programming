# Recursive lcs
def lcs_rec(l1,l2):
	if l1==[] or l2==[]:
		return 0
	elif l1[-1]==l2[-1]:
		return 1+lcs_rec(l1[:-1],l2[:-1])
	else:
		return max(lcs_rec(l1[:-1],l2),lcs_rec(l1,l2[:-1]))
l1=list(input())
l2=list(input())
print(lcs_rec(l1,l2))