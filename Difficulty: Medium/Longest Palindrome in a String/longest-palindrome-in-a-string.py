class Solution:
    def longestPalindrome(self, s):
        start = 0
        maxlen = 1
        
        # Loop over each character in the string as a center of a potential palindrome
        for i in range(1, len(s)):  # Start from index 1 to compare with index 0

            # Even length palindrome
            l = i - 1
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxlen:
                    maxlen = r - l + 1
                    start = l
                l -= 1
                r += 1

            # Odd length palindrome
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxlen:
                    maxlen = r - l + 1
                    start = l
                l -= 1
                r += 1

        return s[start:start + maxlen]


        # code here

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalindrome(S)

        print(ans)
        print("~")
# } Driver Code Ends