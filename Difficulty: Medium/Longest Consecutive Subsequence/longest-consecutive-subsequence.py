 #User function Template for python3
 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        arr.sort()
        current=1
        last=0
        for i in range(1,len(arr)):
            if arr[i]!=arr[i-1]:
                if arr[i]==arr[i-1]+1:
                    current+=1
                else:
                    last=max(last,current)
                    current=1
        return max(last,current)
            
        
        #code here

            
        
        #code here
