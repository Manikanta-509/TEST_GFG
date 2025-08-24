class Solution:
    def findMaxSum(self, arr):
        incl = 0  # loot including previous house
        excl = 0  # loot excluding previous house

        for money in arr:
            new_excl = max(incl, excl)
            incl = excl + money
            excl = new_excl

        return max(incl, excl)
