class Solution:
    def peakElement(self, arr):
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high) // 2

            if arr[mid] > arr[mid + 1]:
                high = mid
            else:
                low = mid + 1

        return low
        # Code here
        