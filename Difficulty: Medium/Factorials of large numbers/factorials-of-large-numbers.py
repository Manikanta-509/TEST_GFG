#User function Template for python3

class Solution:
    def factorial(self, n):
        fact=1
        for i in range(2,n+1):
            fact*=i
        return [int(i) for i in str(fact)]
    
        #code here