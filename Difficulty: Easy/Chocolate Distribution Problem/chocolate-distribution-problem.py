#User function Template for python3

class Solution:

    def findMinDiff(self, arr,M):
        n=len(arr)
        if M>n:
            return False
        arr.sort()
        min_diff=float("inf")
        for i in range(n-M+1):
            diff=arr[i+M-1]-arr[i]
            min_diff=min(diff,min_diff)
        return min_diff
            

        # code here