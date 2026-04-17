class Solution:
    def findMinDiff(self, arr, m):
        n=len(arr)
        if m>n:
            return False
        min_diff=float("inf")
        arr.sort()
        for i in  range(n-m+1):
            dff=arr[i+m-1]-arr[i]
            min_diff=min(min_diff,dff)
        return min_diff
            
            
        # code here