class Solution:
    def findMin(self, arr):
        min_ele=arr[0]
        for i in range(1,len(arr)):
            if arr[i]<min_ele:
                min_ele=arr[i]
        return min_ele
        # Return the minimum value
                
        # code here
        