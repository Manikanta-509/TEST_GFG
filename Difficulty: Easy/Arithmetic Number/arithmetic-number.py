#User function Template for python3

class Solution:
    def inSequence(self, a, b, c):
        if c==0:
            return a==b
        elif(b-a)%c==0 and (b-a)//c>=0:
            return True
        else:
            return False
