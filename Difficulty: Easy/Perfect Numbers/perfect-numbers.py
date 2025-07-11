class Solution:
    def isPerfect(self, n):
        if n <= 1:
            return False
        
        total = 1  # 1 is always a proper divisor (exclude n itself)
        i = 2
        while i * i <= n:
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i
            i += 1
        return total == n
