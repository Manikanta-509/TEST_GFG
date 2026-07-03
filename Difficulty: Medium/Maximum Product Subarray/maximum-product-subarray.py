class Solution:
	def maxProduct(self,arr):
	    min_pr=max_pr=pr=arr[0]
	    for i in range(1,len(arr)):
	        if arr[i]<0:
	            max_pr,min_pr=min_pr,max_pr
	        max_pr=max(arr[i],arr[i]*max_pr)
	        min_pr=min(arr[i],arr[i]*min_pr)
	        pr=max(pr,max_pr,min_pr)
	    return pr
	            # code here
		# code here
		