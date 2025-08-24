class Solution:
    def countSquares(self, n):
        count = 0
        i = 1
        while i * i < n:   # check until square is <= n
            count += 1
            i += 1
        return count

        
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.countSquares(N))
        print("~")

# } Driver Code Ends