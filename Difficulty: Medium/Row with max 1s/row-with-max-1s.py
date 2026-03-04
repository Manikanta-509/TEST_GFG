class Solution:
    def rowWithMax1s(self, arr):
        roe_index=-1
        j=len(arr[0])-1
        for i in range(len(arr)):
            while j>=0 and arr[i][j]==1:
                j-=1
                roe_index=i
        return roe_index