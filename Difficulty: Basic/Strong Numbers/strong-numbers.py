class Solution:
    def fact(self, n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    def isStrong(self, n):
        original = n
        total = 0

        while n > 0:
            digit = n % 10
            total += self.fact(digit)
            n //= 10

        return total == original