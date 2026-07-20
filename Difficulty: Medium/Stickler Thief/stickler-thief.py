class Solution:  
    def findMaxSum(self, arr):
        include=0
        exclude=0
        for i in arr:
            new_include=max(include,exclude)
            include=i+exclude
            exclude=new_include
        return max(include,exclude)