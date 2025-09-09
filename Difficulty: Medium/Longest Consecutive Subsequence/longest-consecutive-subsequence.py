class Solution:
    def longestConsecutive(self, arr):
        if not arr:
            return 0

        arr.sort()
        longest = 1
        current_streak = 1

        for i in range(1, len(arr)):
            # Skip duplicates
            if arr[i] == arr[i-1]:
                continue

            if arr[i] == arr[i-1] + 1:
                # Consecutive element → extend streak
                current_streak += 1
            else:
                # Reset streak
                longest = max(longest, current_streak)
                current_streak = 1

        # Final update
        longest = max(longest, current_streak)
        return longest

        #code here