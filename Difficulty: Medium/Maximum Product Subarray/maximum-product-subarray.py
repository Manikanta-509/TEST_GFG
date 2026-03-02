class Solution:
	def maxProduct(self,arr):
	    min_ele=max_ele=product=arr[0]
	    for i in range(1,len(arr)):
	        if arr[i]<0:
	            max_ele,min_ele=min_ele,max_ele
	        max_ele=max(arr[i],arr[i]*max_ele)
	        min_ele=min(arr[i],arr[i]*min_ele)
	        product=max(max_ele,min_ele,product)
	    return product
		# code here