#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def rearrange(self, arr):
        n = len(arr)
        arr.sort()

        result = [0] * n
        i, j = 0, n - 1
        idx = 0

        while i <= j:
            if idx < n:
                result[idx] = arr[j]
                idx += 1
            if idx < n:
                result[idx] = arr[i]
                idx += 1
            i += 1
            j -= 1

        for i in range(n):
            arr[i] = result[i]


            


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rearrange(arr)
        print(*arr)
        # print("~")
        t -= 1


# } Driver Code Ends