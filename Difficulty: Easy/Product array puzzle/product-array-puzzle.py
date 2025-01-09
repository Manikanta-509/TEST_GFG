#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        result = [1] * n
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= arr[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= arr[i]
        
        return result

        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends