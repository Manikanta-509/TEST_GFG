class Solution:
    def isSorted(self, arr) -> bool:
        n=len(arr)
        for i in range(1,n):
            if arr[i]>=arr[i-1]:
                continue
            else:
                return False
                break
        return True
        # code here
        