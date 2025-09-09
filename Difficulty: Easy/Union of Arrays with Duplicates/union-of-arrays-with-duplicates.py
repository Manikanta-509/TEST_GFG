class Solution:    
    def findUnion(self, a, b):
        seen = {}
        result = []

        # Add elements from first array
        for x in a:
            if x not in seen:
                result.append(x)
                seen[x] = True

        # Add elements from second array
        for x in b:
            if x not in seen:
                result.append(x)
                seen[x] = True

        return result
