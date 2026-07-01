class Solution:
    def findUnion(self, a, b):
        seen={}
        result=[]
        for i in a:
            if i not in seen:
                result.append(i)
                seen[i]=True
        for i in b:
            if i not in seen:
                result.append(i)
                seen[i]=True
        result.sort()
        return result
        # code here 
        