class Solution:
    def maxSubarraySum(self, arr):
        max_le=min_le=mid=arr[0]
        for i in range(1,len(arr)):
            max_le=max(arr[i],max_le+arr[i])
            min_le=max(max_le,min_le)
        return min_le
        # Code here