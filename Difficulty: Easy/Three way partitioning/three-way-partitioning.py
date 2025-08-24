class Solution:
    def threeWayPartition(self, arr, a, b):
        n = len(arr)
        low, mid, high = 0, 0, n - 1
        
        while mid <= high:
            if arr[mid] < a:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] > b:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
            else:
                mid += 1
        
        return arr
