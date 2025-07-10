class Solution:
    def findDuplicates(self, arr):
        seen = set()
        duplicates = set()

        for num in arr:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)

        return sorted(duplicates)

