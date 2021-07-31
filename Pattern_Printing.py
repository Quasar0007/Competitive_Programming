class Solution:
	def printPattern(self, N):
		s=[str(N)]*(2*N-1)
		l=[0]*(2*N-1)
		i=0
		j=2*N-2
		x=str(N)
		while i!=j:
		    for k in range(i,j+1):
		        s[k]=x
		    z=''.join(s)
		    l[i]=z
		    l[j]=z
		    i+=1
		    j-=1
		    x=int(x)-1
		    x=str(x)
		s[i]=str(1)
		z=''.join(s)
		l[i]=z
		for lmao in l:
		    print(lmao)