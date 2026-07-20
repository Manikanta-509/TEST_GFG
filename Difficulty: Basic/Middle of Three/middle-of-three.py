class Solution:
    def middle(self, a, b, c):
        if (a>b and a<c) or (a>c and a<b):
            return a
        elif (b>c and b<a) or (b>a and b<c):
            return b
        else:
            return c
