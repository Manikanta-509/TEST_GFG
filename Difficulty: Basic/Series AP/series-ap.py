
class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        d=a2-a1
        return a1+(n-1)*d
        
