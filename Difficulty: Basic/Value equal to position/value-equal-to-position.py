class Solution:
    def valEqualToPos(self, arr):
        result=[]
        for i in range(len(arr)):
            if arr[i]==i+1:
                result.append(arr[i])
        return result
        # code here
        