class Solution:
    def maxSubarraySum(self, arr):
        left=right=arr[0]
        for i in range(1,len(arr)):
            left=max(arr[i],arr[i]+left)
            right=max(right,left)
        return right
        
        # Code here