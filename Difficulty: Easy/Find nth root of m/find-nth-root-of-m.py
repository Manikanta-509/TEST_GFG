#User function Template for python3

class Solution:
	def nthRoot(self, n: int, m: int) -> int:
        low = 1
        high = m
        while low <= high:
            mid = (low + high) // 2
            power = mid ** n
            if power == m:
                return mid
            elif power < m:
                low = mid + 1
            else:
                high = mid - 1
        return -1

		# Code here