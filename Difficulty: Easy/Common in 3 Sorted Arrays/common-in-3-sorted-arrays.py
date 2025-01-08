#User function Template for python3


#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        x=set(arr1)
        y=set(arr2)
        z=set(arr3)
        a=x&y&z
        return sorted(a)
        
        
        #Code Here

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        crr = list(map(int, input().split()))
        ob = Solution()
        res = ob.commonElements(arr, brr, crr)
        if len(res) == 0:
            print(-1)
        else:
            print(" ".join(map(str, res)))
        print("~")
# } Driver Code Ends