class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        org1,org2=a,b
        while b!=0:
            a,b=b, a%b
        gcd=a
        lcm=(org1*org2)//gcd
        return [lcm,gcd]
        # code here