class Solution:
    def findTwoElement(self, arr):
        rep=miss=0
        freq=[0]*(len(arr)+1)
        for i in arr:
            freq[i]+=1
        for i in range(1,len(arr)+1):
            if freq[i]==0:
                miss=i
            elif freq[i]>1:
                rep=i
        return [rep,miss]
            
        # code here

