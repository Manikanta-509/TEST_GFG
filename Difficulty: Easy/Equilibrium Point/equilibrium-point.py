class Solution:
    def findEquilibrium(self, arr):
        left=0
        total=sum(arr)
        for i in range(len(arr)):
            total-=arr[i]
            if total==left:
                return i
            left+=arr[i]
        return -1
            
        # code here

