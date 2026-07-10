class Solution:
    def findStepKeyIndex(self, arr, k, x):
        for i in range(len(arr)):
            if arr[i]==x:
                return i
                break
        return -1

        
        # code here
