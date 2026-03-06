class Solution:
    def findMedian(self, arr):
        arr.sort()   # Step 1: Sort the array
        
        d = len(arr)
        
        if d % 2 == 0:
            median1 = arr[d//2 - 1]
            median2 = arr[d//2]
            median3 = (median1 + median2) / 2
            return median3
        else:
            return arr[d//2]
        #code here.
