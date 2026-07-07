class Solution:
    def isBinaryPalindrome(self, n):
        a=bin(n)[2:]
        left=0
        right=len(a)-1
        
        while left<right:
            if a[left]!=a[right]:
                return False
                break
            left+=1
            right-=1
        return True

        