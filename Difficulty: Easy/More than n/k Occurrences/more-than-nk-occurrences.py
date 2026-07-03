class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr, k):
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        total=0
        n=len(arr)
        for key in freq:
            if freq[key]>n//k:
                total+=1
        return total
        #Your code here
        