'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def isBST(self, root):
        def bsf(node):
            if not node:
                return True, float('inf'), float('-inf')

            left_bsf, left_min, left_max = bsf(node.left)
            right_bsf, right_min, right_max = bsf(node.right)

            if left_bsf and right_bsf and left_max < node.data < right_min:
                return True, min(left_min, node.data), max(right_max, node.data)
            
            return False, 0, 0

        return bsf(root)[0]

            
        #code here