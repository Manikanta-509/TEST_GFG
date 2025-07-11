class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False  # 0 and 1 are not prime
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

        # code here