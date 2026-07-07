class Solution:
	def isAutomorphic(self, n):
	    sq=n*n
	    while n>0:
	        if n%10!=sq%10:
	            return "Not Automorphic"
	        n//=10
	        sq//=10
	    return "Automorphic"
		# code here
		
