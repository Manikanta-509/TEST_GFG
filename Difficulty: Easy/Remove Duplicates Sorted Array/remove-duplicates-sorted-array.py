class Solution:
    def removeDuplicates(self, arr):
        i=0
        for j in range(1,len(arr)):
            if arr[i]!=arr[j]:
                i+=1
            arr[i]=arr[j]
        return arr[:(i+1)]
        # code here 
        