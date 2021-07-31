class Solution:
    def net(self,n,cout):
        x=0
        while 2**x<=n:
            x+=1
        cout+=1
        return 2**(x-1),cout
	
	def setBits(self, N):
	    cout = 0
		s,cout = self.net(N,cout)
		k=(N-s)
		while k!=0:
		    s,cout = self.net(k,cout)
		    k-=s
		return cout