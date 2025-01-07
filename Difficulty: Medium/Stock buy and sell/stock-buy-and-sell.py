#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function template for Python
 
class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, arr):
	    result=0
	    i=0
	    while i<len(arr)-1:
	        while i<len(arr)-1 and arr[i+1]<=arr[i]:
	            i+=1
	        if i==len(arr)-1:
	            break
	        buy=i
	        i+=1
	        while i<len(arr) and arr[i]>=arr[i-1]:
	            i+=1
	        sell=i-1
	        profit=arr[sell]-arr[buy]
	        result+=profit
	    return result
	        
        # code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.stockBuySell(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends