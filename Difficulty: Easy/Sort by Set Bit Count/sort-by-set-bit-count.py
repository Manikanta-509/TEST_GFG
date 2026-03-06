#User function Template for python3

class Solution:
    def sortBySetBitCount(self, arr, n):
        arr.sort(key=lambda x: bin(x).count('1'), reverse=True)
        return arr
        # Your code goes here