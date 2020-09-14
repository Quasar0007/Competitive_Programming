class CoOrdinates():
	def __init__(self,x,y,z):
		self.xc=x
		self.yc=y
		self.zc=z
	def addition(self,other):
		return (self.xc+other.xc,self.yc+other.yc,self.zc+other.zc)
	def scalarMultiplication(self,k):
		return (k*(self.xc),k*(self.yc),k*(self.zc))
	def dP(self,other):
		return (self.xc)*(other.xc)+(self.yc)*(other.yc)+(self.zc)*(other.zc)
	def cP(self,other):
		return ((self.yc)*(other.zc)-(self.zc)*(other.yc),(other.xc)*(self.zc)-(self.xc)*(other.zc),(self.xc)*(other.yc)-(self.yc)*(other.xc))


