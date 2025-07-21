#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        arr.sort()
        ans=arr[-1]-arr[0]
        for i in range(len(arr)-1):
            max_ele=max(arr[-1]-k,arr[i]+k)
            min_ele=min(arr[0]+k,arr[i+1]-k)
            if min_ele<0:
                continue
            ans=min(ans,max_ele-min_ele)
        return ans
        # code here