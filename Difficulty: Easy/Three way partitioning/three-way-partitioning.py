#User function template for Python

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
	            mid+=1
	            low+=1
	        elif arr[mid]>b:
	            arr[mid],arr[high]=arr[high],arr[mid]
	            high-=1
	        else:
	            mid+=1
	        
	    # code here 