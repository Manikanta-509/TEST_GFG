class Solution:
    def replaceWithRank(self, arr):
        n = len(arr)

        temp = []

        for i in range(n):
            temp.append((arr[i], i))

        temp.sort()

        for rank in range(n):
            value, idx = temp[rank]
            arr[idx] = rank