class Solution:
    def findDuplicate(self, arr):
        seen = set()
        for num in arr:
            if num in seen:
                return num
            seen.add(num)
        return -1  # shouldn't happen

    def findTwoElement(self, arr):
        n = len(arr)
        total = n * (n + 1) // 2
        actual = sum(arr)

        dup = self.findDuplicate(arr)
        miss = dup + total - actual
        return (dup, miss)


        
        # code here

