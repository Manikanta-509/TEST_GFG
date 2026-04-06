class Solution:
    def findEquilibrium(self, arr):
        total_sum=sum(arr)
        left_sum=0
        for i in range(len(arr)):
            total_sum-=arr[i]
            if left_sum==total_sum:
                return i
            left_sum+=arr[i]
        return -1
        # code here

