class Solution:
    def stockBuySell(self, arr):
        result = 0
        i = 0
        n = len(arr)
        while i < n - 1:
            while i < n - 1 and arr[i + 1] <= arr[i]:
                i += 1
            if i == n - 1:
                break
            buy = i
            i += 1
            while i < n and arr[i] >= arr[i - 1]:
                i += 1
            sell = i - 1
            result += arr[sell] - arr[buy]
        return result