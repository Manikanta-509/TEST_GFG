class Solution:
    def findDuplicates(self, arr):
        duplicate=set()
        seen=set()
        for i in arr:
            if i in seen:
                duplicate.add(i)
            else:
                seen.add(i)
        return list(duplicate)
        # code here
        