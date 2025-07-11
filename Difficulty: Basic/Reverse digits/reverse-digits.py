#User function Template for python3

class Solution:
	def reverseDigits(self, n):
	    if n<0:
	        return -int(str(-n)[::-1].lstrip('0'))
        else:
            return int(str(n)[::-1].lstrip('0'))
		# Code here