class Solution:
    def missingNum(self, arr):
        n=len(arr)
        a=(n+1)*(n+2)//2
        b=sum(arr)
        return a-b
        # code here
        