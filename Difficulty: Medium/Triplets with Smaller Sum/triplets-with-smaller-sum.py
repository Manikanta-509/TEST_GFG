class Solution:
    def countTriplets(self, n, sum, arr):
        arr.sort()
        result=0
        for i in range(n-2):
            j=i+1
            end=n-1
            while j<end:
                total_sum=arr[i]+arr[j]+arr[end]
                if total_sum<sum:
                    result+=(end-j)
                    j+=1
                else:
                    end-=1
        return result
        #code here


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(0, t):
    l = list(map(int, input().split()))
    n = l[0]
    k = l[1]
    a = list(map(int, input().split()))
    ob = Solution()
    ans = ob.countTriplets(n, k, a)
    print(ans)

    print("~")
# } Driver Code Ends