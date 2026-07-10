class Solution:
    def countSquares(self, n):
        count=0
        for i in range(1,n):
            if i**2<n:
                count+=1
            else:
                break
        return count
        # code here 
        