#User function Template for python3

class Solution:
    
    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x):
        rows=len(matrix)
        cols=len(matrix[0]) if rows >0 else 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==x:
                    return 1
        return 0
    	# code here 
    	
