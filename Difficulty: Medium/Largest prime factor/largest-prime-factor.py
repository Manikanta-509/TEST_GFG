class Solution:
    def largestPrimeFactor(self, n):
        max_prime = -1

        # Remove all 2s
        if n % 2 == 0:
            max_prime = 2
            while n % 2 == 0:
                n //= 2

        # Check odd numbers starting from 3
        i = 3
        while i * i <= n:
            if n % i == 0:
                max_prime = i
                while n % i == 0:
                    n //= i
            i += 2

        # If the remaining number is greater than 2, it's a prime
        if n > 2:
            max_prime = n

        return int(max_prime)
