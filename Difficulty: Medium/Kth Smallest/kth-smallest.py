class Solution:
    def merge(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2

            left = arr[:mid]
            right = arr[mid:]

            self.merge(left)
            self.merge(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        return arr

    def kthSmallest(self, arr, k):
        self.merge(arr)
        return arr[k - 1]
        # Code here
        
