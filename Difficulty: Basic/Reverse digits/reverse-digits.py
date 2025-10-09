#User function Template for python3

class Solution:
	def reverseDigits(self, n):
	    rev=0
	    while n>0:
	        total=n%10
	        rev=rev*10+total
	        n=n//10
	    return rev
		# Code here