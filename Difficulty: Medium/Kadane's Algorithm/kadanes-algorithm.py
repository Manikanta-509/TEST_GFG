class Solution:
    def maxSubarraySum(self, arr):
        left=right=arr[0]
        for i  in range(1,len(arr)):
            if arr[i]>left+arr[i]:
                left=arr[i]
            else:
                left=left+arr[i]
            if right<left:
                right=left
        return right
        # Code here
        