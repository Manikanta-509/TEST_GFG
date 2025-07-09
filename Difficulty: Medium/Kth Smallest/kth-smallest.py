#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        arr.sort()
        return arr[k-1]
        
        
