class Solution:  
    def findMaxSum(self, arr):
        incl=0
        excul=0
        for i in arr:
            new_incl=max(incl,excul)
            incl=i+excul
            excul=new_incl
        return max(incl,excul)
        