class Solution:
    def middle(self, a, b, c):
        if (a>b and a<c) or (a>c and a<b):
            return a
        elif (b>a and b<c) or (b>c and b<a):
            return b
        else:
            return c
        #code here
