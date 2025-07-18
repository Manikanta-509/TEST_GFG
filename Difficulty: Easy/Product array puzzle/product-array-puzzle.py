#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        result = [1] * n

        # Compute left product for each element
        left = 1
        for i in range(n):
            result[i] = left
            left *= arr[i]

        # Compute right product and multiply with result
        right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= arr[i]

        return result

        #code here