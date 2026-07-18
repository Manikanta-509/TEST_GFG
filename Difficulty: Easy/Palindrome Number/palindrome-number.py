class Solution:
    def isPalindrome(self, n):
        sign=-1 if n<0 else 1
        n=abs(n)
        org=n
        rev=0
        while n!=0:
            digit=n%10
            rev=(rev*10+digit)
            n=n//10
        rev=rev*sign
        org=org*sign
        return rev==org