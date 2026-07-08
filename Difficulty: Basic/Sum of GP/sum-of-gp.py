class Solution:
    def sumOfGP(self, n, a, r):
        
        if r==1:
        #code here
            return a * n
        return (a * (r**n - 1)) // (r - 1)