class Solution:
    def leaders(self, arr):
        n=len(arr)
        max_leader=arr[-1]
        leader=[max_leader]
        for i in range(n-2,-1,-1):
            if arr[i]>=max_leader:
                max_leader=arr[i]
                leader.append(arr[i])
        leader.reverse()
        return leader