class Solution:
    def getMinMax(self, arr):
        max_ele=arr[0]
        min_ele=arr[0]
        for i in range(1,len(arr)):
            if arr[i]<min_ele:
                min_ele=arr[i]
            if arr[i]>max_ele:
                max_ele=arr[i]
        return min_ele,max_ele# code here
        