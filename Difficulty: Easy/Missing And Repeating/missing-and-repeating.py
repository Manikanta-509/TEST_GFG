class Solution:
    def duplicates(self, arr):
        seen = set()
        for i in arr:
            if i in seen:
                return i
            seen.add(i)

    def findTwoElement(self, arr):
        n = len(arr)
        duplicate = self.duplicates(arr)

        total = n * (n + 1) // 2
        missing = total - (sum(arr) - duplicate)

        return [duplicate, missing]
        
        # code here

