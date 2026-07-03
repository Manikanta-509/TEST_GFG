class Solution:
    def findDuplicates(self, arr):
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        result=[]
        for key in freq:
            if freq[key]>1:
                result.append(key)
        return result
            
        # code here
        