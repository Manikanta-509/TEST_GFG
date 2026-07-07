class Solution:
    def removeDuplicate(self, arr):
        seen=set()
        result=[]
        for i in arr:
            if i not in seen:
                result.append(i)
                seen.add(i)
        return result
        # code here
    

