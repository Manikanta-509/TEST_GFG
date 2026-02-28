class Solution:
    def nthRoot(self, n, m):
        if m==0:
            return 0
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
       
