class Solution:
    def getSecondLargest(self, arr):
        max_ele = float("-inf")
        second_max = float("-inf")
        
        for i in arr:
            if i > max_ele:
                second_max = max_ele
                max_ele = i
            elif i > second_max and i != max_ele:
                second_max = i
        
        # If there is no second largest element (like all elements same)
        if second_max == float("-inf"):
            return -1
        return second_max
        # Code Here