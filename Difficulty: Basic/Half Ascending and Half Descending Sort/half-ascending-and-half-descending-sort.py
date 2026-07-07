class Solution:
    def customSort(self, arr):
        n = len(arr)
        arr[:n//2] = sorted(arr[:n//2])
        arr[n//2:] = sorted(arr[n//2:], reverse=True)
        return arr
        