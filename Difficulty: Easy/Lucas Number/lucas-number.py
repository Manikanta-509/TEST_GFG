#User function Template for python3

class Solution:
    def lucas(self, n):
        if n==0:
            return 2
        if n==1:
            return 1
        mod=1000000007
        a=2
        b=1
        for i in range(2,n+1):
            c=(a+b)%mod
            a=b
            b=c
        return b
        # code here 