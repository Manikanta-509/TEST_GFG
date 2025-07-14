class Solution:
    def removeDuplicates(self, arr):
        if not arr:
            return 0
        i=0

        for j in range(1, len(arr)):
            if arr[j] != arr[i]:
                i += 1
                arr[i] = arr[j]

        return i + 1  
