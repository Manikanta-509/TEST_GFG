class Solution:
    def countFreq(self, arr):
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        result=[]
        for key in freq.items():
            result.append(key)
        return result
            
        #code here
        