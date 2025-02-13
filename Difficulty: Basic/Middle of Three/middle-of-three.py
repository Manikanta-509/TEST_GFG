#User function Template for python3

class Solution:
    def middle(self, a, b, c):
        nums=[a,b,c]
        nums.sort()
        return nums[1]
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = int(input())
        B = int(input())
        C = int(input())
        ob = Solution()
        print(ob.middle(A, B, C))
        print("~")

# } Driver Code Ends