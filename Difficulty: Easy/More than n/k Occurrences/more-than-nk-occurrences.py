#User function Template for python3


class Solution:
    def countOccurence(self, arr, k):
        n=len(arr)
        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        count=0
        for key in freq:
            if freq[key]>n//k:
                count+=1
        return count
            
        
        #Your code here