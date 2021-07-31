class Solution:
	def isSame(self, s):
	    for i in range(len(s)):
	        if s[i].isnumeric():
	            if len(s[:i])==int(s[i:]):
	                return 1
	            else:
	                return 0