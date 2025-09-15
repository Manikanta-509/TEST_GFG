'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def getCount(self, root, l, h):
        if not root:
            return 0
        
        # If root is in range
        if root.data <= h and root.data >= l:
            return (1 
                    + self.getCount(root.left, l, h) 
                    + self.getCount(root.right, l, h))
        
        # If root's value is smaller than l, only right subtree may have nodes
        elif root.data < l:
            return self.getCount(root.right, l, h)
        
        # If root's value is greater than h, only left subtree may have nodes
        else:
            return self.getCount(root.left, l, h)


        # Your code here