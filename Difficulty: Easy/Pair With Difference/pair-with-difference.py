
from typing import List


class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        arr.sort()
        left=0
        right=1
        while right<len(arr):
            if left==right:
                right+=1
                continue
            diff=arr[right]-arr[left]
            if diff==x:
                return True
            elif diff<x:
                right+=1
            else:
                left+=1
        return False