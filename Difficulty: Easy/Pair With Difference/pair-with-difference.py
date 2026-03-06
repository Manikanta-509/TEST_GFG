
from typing import List


from typing import List

class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        s = set()

        for num in arr:
            if (num + x) in s or (num - x) in s:
                return True
            s.add(num)

        return False
                


        


        
        # code here
        
