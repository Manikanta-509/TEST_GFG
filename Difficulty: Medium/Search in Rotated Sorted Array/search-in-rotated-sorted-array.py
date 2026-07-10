class Solution:
    def search(self, arr, key):
        for i in range(len(arr)):
            if arr[i]==key:
                return i
        return -1
        # code here
        