class Solution:
    def getMinMax(self, arr):
        max_ele=arr[0]
        min_ele=arr[0]
        for i in arr:
            if i>max_ele:
                max_ele=i
            if i<min_ele:
                min_ele=i
        return (min_ele,max_ele)

        # code here