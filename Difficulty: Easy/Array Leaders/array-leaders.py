class Solution:
    def leaders(self, arr):
        n=len(arr)
        result=[]
        max_leader=arr[-1]
        result.append(max_leader)
        for i in range(n-2,-1,-1):
            if arr[i]>=max_leader:
                max_leader=arr[i]
                result.append(arr[i])
        result.reverse()
        return result
        