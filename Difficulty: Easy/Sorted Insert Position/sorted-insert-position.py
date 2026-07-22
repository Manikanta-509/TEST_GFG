class Solution:
    def searchInsertK(self, arr, k):
        low=0
        high=len(arr)-1
        ans=len(arr)
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
            