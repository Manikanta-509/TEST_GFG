class Solution:
    def maxProduct(self, arr):
        max_ele = min_ele = product = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < 0:
                max_ele, min_ele = min_ele, max_ele   # swap
            max_ele = max(arr[i], max_ele * arr[i])
            min_ele = min(arr[i], min_ele * arr[i])
            product = max(product, max_ele)
        return product
