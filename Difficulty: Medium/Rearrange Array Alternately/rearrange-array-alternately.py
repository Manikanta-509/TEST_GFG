
class Solution:
    def rearrange(self, arr):
        arr.sort()
        n=len(arr)
        result=[0]*n
        i=0
        j=n-1
        idx=0
        while i<=j:
            if idx<n:
                result[idx]=arr[j]
                idx+=1
            if idx<n:
                result[idx]=arr[i]
                idx+=1
            i+=1
            j-=1
        for i in range(n):
            arr[i]=result[i]

            