class Solution:
	def reverseDigits(self, n):
	    rev=0
	    while n>0:
	        digit=n%10
	        rev=rev*10+digit
	        n//=10
	    return rev
	    
		# Code here
		