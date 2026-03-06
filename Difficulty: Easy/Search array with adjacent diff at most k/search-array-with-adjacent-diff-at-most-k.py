#User function Template for python3

class Solution:
    def findStepKeyIndex(self, arr, k, x):
        for i in range(len(arr)):
            if arr[i]==x:
                return i
        return -1
        # code here
