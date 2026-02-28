class Solution:
    def sumOfDigits(self, n):
        a=str(n)
        total=0
        for i in a:
            total+=int(i)
        return total
        # code here