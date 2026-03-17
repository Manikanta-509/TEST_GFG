#User function Template for python3
class Solution:

	
	def removeDuplicates(self, s):
	    result=''
	    seen=set()
	    for i in s:
	        if i not in seen:
	            result+=i
	            seen.add(i)
	    return result
	    # code here