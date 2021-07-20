class Solution:
	def isPlaindrome(self, S):
	    i=0
	    j=len(S)-1
	    while i<j:
	        if S[i]==S[j]:
	             i+=1
	             j-=1
	             continue
	             
	        else:
	            return 0
	    return 1
	           