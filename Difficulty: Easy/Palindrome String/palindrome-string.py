#User function Template for python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        b="".join(reversed(s))
        if b==s:
            return True
        return False
		# code here