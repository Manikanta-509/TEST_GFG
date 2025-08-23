class Solution:
    def sort012(self, arr):
        left=0
        mid=0
        high=len(arr)-1
        while mid<=high:
            if arr[mid]==0:
                arr[left],arr[mid]=arr[mid],arr[left]
                left+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[mid],arr[high]=arr[high],arr[mid]
                high-=1
        return arr
                
        # code here
        