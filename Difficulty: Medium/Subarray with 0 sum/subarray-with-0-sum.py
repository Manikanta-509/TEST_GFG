#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        sub_array={}
        current=0
        for i in range(len(arr)):
            current+=arr[i]
            if current==0 or current in sub_array:
                return True
            sub_array[current]=i
        return False
        ##Your code here
        #Return true or false