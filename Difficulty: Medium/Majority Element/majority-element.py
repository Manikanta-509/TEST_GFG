class Solution:
    def majorityElement(self, arr):
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in freq:
            if freq[i]>len(arr)//2:
                return i
        return -1
        