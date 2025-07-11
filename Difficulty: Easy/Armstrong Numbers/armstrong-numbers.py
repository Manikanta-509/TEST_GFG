#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        digits=str(n)
        a=len(digits)
        total=sum(int(d)**a for d in digits)
        if total==n:
            return True
        return False
        
        # code here 