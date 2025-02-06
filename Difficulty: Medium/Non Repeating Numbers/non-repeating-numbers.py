#User function Template for python3

class Solution:
	def singleNumber(self, arr):
        seen=set()
        duplicates=set()
        for i in arr:
            if i in seen:
                duplicates.add(i)
            else:
                seen.add(i)
        return sorted(list(seen-duplicates))
		# Code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNumber(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends