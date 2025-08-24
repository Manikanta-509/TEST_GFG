#User function Template for python3

class Solution:
    def findPermutation(self, s):
        result = []

        def backtrack(path, remaining):
            if not remaining:  # no characters left → a permutation is ready
                result.append(path)
                return
            
            used = set()  # keep track of characters used at this recursion level
            for i in range(len(remaining)):
                if remaining[i] in used:
                    continue  # skip duplicate characters at this level
                used.add(remaining[i])
                # choose remaining[i] and recurse
                backtrack(path + remaining[i], remaining[:i] + remaining[i+1:])

        backtrack("", s)
        return result



        # Code here
        
