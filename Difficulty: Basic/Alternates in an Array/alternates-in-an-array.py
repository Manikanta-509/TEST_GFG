class Solution:
    def getAlternates(self, arr):
        result=[]
        a=len(arr)
        for i in range(0,a,2):
            result.append(arr[i])
        return result
        # Code Here