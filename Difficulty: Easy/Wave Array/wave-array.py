class Solution:
    def sortInWave(self, arr):
        n = len(arr)
        for i in range(0, n-1):
            if i % 2 == 1 and arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            if i % 2 == 0 and arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        return arr

        
        # code here
        
