class Solution:
    def setAllRangeBits(self, N, L, R):
        mask = ((1 << R) - 1) - ((1 << (L - 1)) - 1)
        return N | mask
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,L,R=map(int,input().split())
        
        ob = Solution()
        print(ob.setAllRangeBits(N,L,R))
        print("~")
# } Driver Code Ends