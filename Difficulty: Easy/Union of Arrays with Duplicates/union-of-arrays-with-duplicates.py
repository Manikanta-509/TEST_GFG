class Solution:    
    def findUnion(self, a, b):
        seen={}
        result=[]
        for x in a:
            if x not in seen:
                result.append(x)
                seen[x]=True
        for x in b:
            if x not in seen:
                result.append(x)
                seen[x]=True
        return seen