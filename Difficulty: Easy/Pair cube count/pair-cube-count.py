#User function Template for python3

class Solution:
    def pairCubeCount(self, n):
        count = 0
        for a in range(1, int(n ** (1/3)) + 2):  # a ≥ 1
            a_cubed = a ** 3
            for b in range(0, int(n ** (1/3)) + 2):  # b ≥ 0
                b_cubed = b ** 3
                if a_cubed + b_cubed == n:
                    count += 1
        return count

        # code here 