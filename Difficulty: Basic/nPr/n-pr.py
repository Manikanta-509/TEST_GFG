#User function Template for python3

class Solution:
    def fact(self,n):
        fact=1
        for i in range(2,n+1):
            fact*=i
        return fact
    def nPr(self, n, r):
        if r>n:
            return 0
        return self.fact(n)//self.fact(n-r)

        # code here