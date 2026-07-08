class Solution:
    def arranged(self,arr):
        result=[0]*len(arr)
        pos=0
        neg=1
        for i in range(len(arr)):
            if arr[i]>=0:
                result[pos]=arr[i]
                pos+=2
            else:
                result[neg]=arr[i]
                neg+=2
        return result
        #Code here
        