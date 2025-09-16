'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def LCA(self, root, n1, n2):
        if root is None:
            return None
        
        # if n1 and n2 are Node objects, take their .data
        if isinstance(n1, Node):
            n1 = n1.data
        if isinstance(n2, Node):
            n2 = n2.data
        
        if root.data < n1 and root.data < n2:
            return self.LCA(root.right, n1, n2)
        
        if root.data > n1 and root.data > n2:
            return self.LCA(root.left, n1, n2)
        
        return root

        
    