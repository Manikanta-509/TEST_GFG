#User function Template for python3


class Solution:
    def factorial(self, n):
        if n < 0:
            return -1  # Factorial not defined for negative numbers
        elif n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

        # code here