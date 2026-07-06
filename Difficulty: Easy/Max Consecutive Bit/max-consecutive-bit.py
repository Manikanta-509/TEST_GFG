class Solution:
    def maxConsecBits(self, arr):
        max_const=1
        const=1
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                const+=1
            else:
                max_const=max(max_const,const)
                const=1
        max_const=max(max_const,const)
        return max_const
        #code here 
        