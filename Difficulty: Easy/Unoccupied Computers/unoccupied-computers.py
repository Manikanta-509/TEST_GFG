#User function Template for python3


class Solution:
    def solve(self, n, s):
        in_cafe = set()     # customers currently inside with a computer
        waiting = set()     # customers who walked away
        occupied = 0
        ans = 0

        for ch in s:
            if ch not in in_cafe and ch not in waiting:  # first arrival
                if occupied < n:
                    occupied += 1
                    in_cafe.add(ch)
                else:
                    ans += 1
                    waiting.add(ch)
            elif ch in in_cafe:  # departure of served customer
                occupied -= 1
                in_cafe.remove(ch)
            else:
                # departure of customer who walked away → just ignore
                waiting.remove(ch)

        return ans
