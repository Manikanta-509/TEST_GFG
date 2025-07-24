class Solution:
    def findPages(self, arr, k):
        if k > len(arr):
            return -1  # Not enough books

        low = max(arr)
        high = sum(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2
            student_count = 1
            current_sum = 0
            possible = True

            for pages in arr:
                if current_sum + pages > mid:
                    student_count += 1
                    current_sum = pages
                    if student_count > k:
                        possible = False
                        break
                else:
                    current_sum += pages

            if possible:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
