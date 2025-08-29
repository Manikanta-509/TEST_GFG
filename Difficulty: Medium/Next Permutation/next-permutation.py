#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        pivot = -1
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break
        if pivot == -1:
            arr.reverse()
            return arr
        for i in range(n - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break
        arr[pivot + 1:] = reversed(arr[pivot + 1:])
        
        return arr

                
            
        # code here
