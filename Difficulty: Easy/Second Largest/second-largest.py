class Solution:
    def getSecondLargest(self, arr):
        a=list(set(arr))
        if len(a)<2:
            return -1
        a.sort()
        return a[-2]
            
        
        # Code Here

        # Code Here