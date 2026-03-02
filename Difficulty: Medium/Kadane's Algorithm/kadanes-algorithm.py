class Solution:
    def maxSubarraySum(self, arr):
        max_ele=min_ele=arr[0]
        for i in range(1,len(arr)):
            max_ele=max(arr[i],max_ele+arr[i])
            min_ele=max(max_ele,min_ele)
        return min_ele
        # Code here