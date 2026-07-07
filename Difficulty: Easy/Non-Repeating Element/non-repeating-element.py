class Solution:
    def firstNonRepeating(self, arr): 
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for key in freq:
            if freq[key]==1:
                return key
        return 0
                
        # code here
