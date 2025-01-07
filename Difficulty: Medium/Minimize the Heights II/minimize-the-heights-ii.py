#User function Template for python3

#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        arr.sort()
        ans=arr[-1]-arr[0]
        for i in range(len(arr)-1):
            max_value=max(arr[-1]-k,arr[i]+k)
            min_value=min(arr[0]+k,arr[i+1]-k)
            if min_value<0:
                continue
            ans=min(ans,max_value-min_value)
        return ans
        #User function Template for python3

            
        # code here

  
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends