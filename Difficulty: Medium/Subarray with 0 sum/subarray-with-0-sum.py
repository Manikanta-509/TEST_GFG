class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        array={}
        curr=0
        for i in range(len(arr)):
            curr+=arr[i]
            if curr==0 or curr in array:
                return True
            array[curr]=i
        return False
        ##Your code here
        #Return true or false