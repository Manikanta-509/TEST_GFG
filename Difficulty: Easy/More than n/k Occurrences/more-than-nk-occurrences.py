#User function Template for python3


class Solution:
    def countOccurence(self, arr, k):
        n = len(arr)
        freq = {} 

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        count = 0
        for key in freq:
            if freq[key] > n // k:
                count += 1

        return count

            
        
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countOccurence(A, D)
        print(ans)
        print("~")
# } Driver Code Ends