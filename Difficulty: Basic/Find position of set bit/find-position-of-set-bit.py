#User function Template for python3
class Solution:
    def findPosition(self, n):
        if n == 0 or (n & (n - 1)) != 0:
            return -1
        pos = 1
        while n > 1:
            n >>= 1  # Right shift (divide by 2)
            pos += 1
        return pos
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.findPosition(N))

# } Driver Code Ends