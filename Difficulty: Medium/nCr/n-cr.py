class Solution:
    def factorial(self,n):
        result=1
        for i in range(2,n+1):
            result*=i
        return result
    def nCr(self, n, r):
        if r>n:
            return 0
        return self.factorial(n)//(self.factorial(n-r)*self.factorial(r))
        # code herehttps://media.geeksforgeeks.org/img-practice/chatIcon-1653561581.svg