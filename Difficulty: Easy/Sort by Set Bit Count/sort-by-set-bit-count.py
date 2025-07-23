#User function Template for python3

class Solution:
    def sortBySetBitCount(self, arr, n):
        # Sort by number of set bits in descending order
        arr.sort(key=lambda x: bin(x).count('1'), reverse=True)
        return arr

        
        # Your code goes here