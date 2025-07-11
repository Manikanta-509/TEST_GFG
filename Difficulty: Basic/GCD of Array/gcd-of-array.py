#User function Template for python3

class Solution:
    def find(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def gcd(self, n, arr):
        result = arr[0]
        for i in range(1, n):
            result = self.find(result, arr[i])
        return result

                
        # code here 