class Solution:
    def isPalindrome(self, n):
        original = abs(n)
        n = abs(n)

        rev = 0

        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10

        return rev == original
		