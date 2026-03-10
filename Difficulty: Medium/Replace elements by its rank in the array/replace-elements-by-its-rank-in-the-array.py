#User function Template for python3

class Solution:
    def replaceWithRank(self, N, arr):
        sorted_arr = sorted(arr)
        rank = 1
        result = {}
        for num in sorted_arr:
            if num not in result:
                result[num] = rank
                rank += 1
        a = [result[num] for num in arr]
        return a
        # Code here