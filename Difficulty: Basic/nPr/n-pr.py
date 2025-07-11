#User function Template for python3

class Solution:
    def factorial(self,n):
        result=1
        for i in range(2,n+1):
            result*=i
        return result
    def nPr(self, n, r):
        if r>n:
            return 1
        return self.factorial(n)//self.factorial(n-r)
        
        
        # code here