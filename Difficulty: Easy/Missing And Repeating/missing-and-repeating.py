#User function Template for python3

class Solution:
    def findTwoElement( self,arr):
        repated=missing=0
        freq=[0]*(len(arr)+1)
        for i in arr:
            freq[i]+=1
        for i in range(1,len(arr)+1):
            if freq[i]==0:
                missing=i
            elif freq[i]>1:
                repated=i
        return [repated,missing]
                
        # code here



        # code here

