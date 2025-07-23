
class Solution:
    def majorityElement(self, arr):
        n = len(arr)
        count = 0
        candidate = None

        # Step 1: Find candidate
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # Step 2: Verify candidate
        if arr.count(candidate) > n // 2:
            return candidate
        else:
            return -1
      #code here
        #code here