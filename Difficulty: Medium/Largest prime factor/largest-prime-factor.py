
class Solution:
    def largestPrimeFactor(self, n):
        max_prime=-1
        if n%2==0:
            max_prime=2
            while n%2==0:
                n//=2
        i=3
        while i*i<=n:
            if n%i==0:
                max_prime=i
                while n%i==0:
                    n//=i
            i+=2
        if n>2:
            max_prime=n
        return int(max_prime)
            
        # code here
        