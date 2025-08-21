'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = -1
        
        def inorder(node):
            if not node or self.count >= k:
                return
            
            # 1. Traverse left
            inorder(node.left)
            
            # 2. Visit node
            self.count += 1
            if self.count == k:
                self.result = node.data
                return
            
            # 3. Traverse right
            inorder(node.right)
        
        inorder(root)
        return self.result
