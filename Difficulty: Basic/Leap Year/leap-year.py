class Solution:
    def checkYear (self, n):
        if n%4==0 and n%100!=0 or n%400==0:
            return True
        return False
        # code here
        