class Solution:
    def getSecondLargest(self, arr):
        max1=float('-inf')
        max2=float('-inf')
        for i in range(len(arr)):
            if arr[i]>max1:
                max2=max1
                max1=arr[i]
            elif arr[i]>max2 and arr[i]!=max1:
                max2=arr[i]
        if max2==float('-inf'):
                return -1
        return max2