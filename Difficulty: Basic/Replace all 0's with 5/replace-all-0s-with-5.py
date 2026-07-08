class Solution:
    def convertFive(self, n):
        if n==0:
            return 5
        rev=0
        while n>0:
            digit=n%10
            if digit==0:
                digit=5
            rev=rev*10+digit
            n//=10
        result=0
        while rev>0:
            digit=rev%10
            result=result*10+digit
            rev//=10
        return result
        
        # code here
        