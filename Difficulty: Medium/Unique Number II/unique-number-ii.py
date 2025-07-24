#User function Template for python3
#User function Template for python3

class Solution:
    def singleNum(self, arr):
        seen=set()
        duplicates=set()
        for i in arr:
            if i in seen:
                duplicates.add(i)
            else:
                seen.add(i)
        return sorted(list(seen-duplicates))
        # Code here


		# Code here
