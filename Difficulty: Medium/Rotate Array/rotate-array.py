class Solution:
    def rotateArr(self, arr, d):
        n=len(arr)
        k=d%n
        left=0
        right=k-1
        while left<=right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        left=k
        right=n-1
        while left<=right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        left=0
        right=n-1
        while left<=right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        return arr
        #code here
        