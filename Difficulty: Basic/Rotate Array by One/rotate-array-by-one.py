#User function Template for python3

class Solution:
    def rotate(self, arr):
        if len(arr)>1:
            last=arr.pop()
            arr.insert(0,last)
        return arr
        
    
