class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, arr, a, b):
	    low=0
	    mid=0
	    high=len(arr)-1
	    while mid<=high:
	        if arr[mid]<a:
	            arr[low],arr[mid]=arr[mid],arr[low]
	            low+=1
	            mid+=1
	        elif  arr[mid]<=b:
	            mid+=1
	        else:
	            arr[high],arr[mid]=arr[mid],arr[high]
	            high-=1
	    return arr

	    # code here 
	    