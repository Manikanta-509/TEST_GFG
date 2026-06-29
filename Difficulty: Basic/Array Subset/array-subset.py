class Solution:
    def isSubset(self, a, b):
        freq = {}

        # Count frequency of elements in a
        for i in a:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        # Check elements of b
        for i in b:
            if i not in freq or freq[i] == 0:
                return False
            freq[i] -= 1

        return True
        # Your code here
    
    
    
    
