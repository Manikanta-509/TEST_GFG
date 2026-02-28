#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        a=str(n)
        b=len(a)
        total=sum(int(i)**b for i in a)
        if total==n:
            return True
        return False
        # code here 