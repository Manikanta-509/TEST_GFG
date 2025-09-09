class Solution:
    def maxSubarraySum(self, arr):
        left = right = arr[0]   # initialize with first element

        for i in range(1, len(arr)):
            # left = max(arr[i], arr[i] + left)
            if arr[i] > arr[i] + left:
                left = arr[i]
            else:
                left = arr[i] + left

            # right = max(right, left)
            if right < left:
                right = left

        return right
