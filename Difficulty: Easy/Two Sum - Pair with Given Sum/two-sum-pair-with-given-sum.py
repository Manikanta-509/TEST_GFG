class Solution:
    def twoSum(self, arr, target):
        arr.sort()
        left = 0
        right = len(arr) - 1

        while left < right:
            current = arr[left] + arr[right]

            if current == target:
                return True
            elif current < target:
                left += 1
            else:
                right -= 1

        return False

		# code here