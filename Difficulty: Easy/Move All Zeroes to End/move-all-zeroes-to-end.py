class Solution:
	def pushZerosToEnd(self, arr):
	    n=len(arr)
	    idx=0
	    for i in range(len(arr)):
	        if arr[i]!=0:
	            arr[idx],arr[i]=arr[i],arr[idx]
	            idx+=1
	    return arr