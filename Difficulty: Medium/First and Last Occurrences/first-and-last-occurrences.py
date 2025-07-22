#User function Template for python3

#User function Template for python3


class Solution:
    def find(self, arr, x):
        left, right = 0, len(arr) - 1
        first, last = -1, -1

        # Find the first occurrence
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                first = mid
                right = mid - 1  # Continue searching in the left half
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        # Reset left and right pointers
        left, right = 0, len(arr) - 1

        # Find the last occurrence
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                last = mid
                left = mid + 1  # Continue searching in the right half
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        # Return result
        if first == -1:  # If `x` is not found
            return [-1, -1]
        return [first, last]

        

        # code here

        
        
        
        # code here