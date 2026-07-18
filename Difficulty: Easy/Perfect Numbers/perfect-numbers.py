class Solution:
    def isPerfect(self, n):
        total=0
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                if i**i==n or i==1:
                    total+=i
                else:
                    total+=i+n//i
        return total==n
            
            
        # code here 
        