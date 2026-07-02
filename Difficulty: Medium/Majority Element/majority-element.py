class Solution:
    def majorityElement(self, arr):
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for key in freq:
            if freq[key]>len(arr)//2:
                return key
        return -1
        #code here
        