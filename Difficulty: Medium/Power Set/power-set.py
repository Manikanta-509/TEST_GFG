#User function Template for python3
class Solution:
    def AllPossibleStrings(self, s):
        n = len(s)
        total_subsequences = (1 << n) 
        result = []
        for i in range(1, total_subsequences): 
            sub = ""
            for j in range(n):
                if i & (1 << j): 
                    sub += s[j]
            result.append(sub) 
        
        return sorted(result) 

		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ob = Solution()
        ans = ob.AllPossibleStrings(s)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends