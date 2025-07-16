class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        for j in range(1, n - 1):
            for i in range(j):
                if arr[i] < arr[j]:
                    for k in range(j + 1, n):
                        if arr[j] < arr[k]:
                            return [arr[i], arr[j], arr[k]]  # Valid triplet
        return [] 
