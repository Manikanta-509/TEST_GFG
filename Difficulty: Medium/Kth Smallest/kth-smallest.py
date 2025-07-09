#User function Template for python3

class Solution:
    def merge(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.merge(left)
            self.merge(right)

            i = j = k = 0

            # Merge left and right arrays
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            # Copy remaining elements from left
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            # Copy remaining elements from right
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

    def kthSmallest(self, arr, k):
        self.merge(arr)           # Sort using merge sort
        return arr[k - 1]         # Return the k-th smallest element

            
        


        
        