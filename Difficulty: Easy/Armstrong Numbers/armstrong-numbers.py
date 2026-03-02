#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        a=str(n)
        b=len(a)
        c=sum(int(i)**b for i in a)
        if c==n:
            return True
        return False