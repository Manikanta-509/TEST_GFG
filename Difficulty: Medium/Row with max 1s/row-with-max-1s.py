class Solution:
    def rowWithMax1s(self, arr):
        row_index=-1
        j=len(arr[0])-1
        for i in range(len(arr)):
            while j>=0 and arr[i][j]==1:
                j-=1
                row_index=i
        return row_index

