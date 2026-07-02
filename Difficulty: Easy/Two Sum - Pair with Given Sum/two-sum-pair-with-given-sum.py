class Solution:
	def twoSum(self, arr, target):
	    arr.sort()
	    left=0
	    right=len(arr)-1
	    while left<right:
	        curr=arr[left]+arr[right]
	        if curr==target:
	            return True
	        elif curr<target:
	            left+=1
	        else:
	            right-=1
	    return False
	            
		# code here