# Implement a class for sets contaning integers.Provide methods for set union and set intersection and give their time compplexity.

class IntSet():
	def __init__(self,l):
		self.ListOfIntegers=l
	def uni(self,other):
		for _ in range(len(self.ListOfIntegers)):
			if self.ListOfIntegers[_] not in other.ListOfIntegers:
				other.ListOfIntegers.append(self.ListOfIntegers[_])
		return other.ListOfIntegers
	def intrsctn(self,other):
		m=[]
		for _ in range(len(self.ListOfIntegers)):
			if self.ListOfIntegers[_] in other.ListOfIntegers:
				m.append(self.ListOfIntegers[_])
		return m

		


