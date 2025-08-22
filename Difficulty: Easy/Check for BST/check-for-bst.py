'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Function to check whether a Binary Tree is BST or not.
    def __init__(self):
        self.prev = float('-inf')   # to track previous inorder value

    def isBST(self, root):
        if root is None:
            return True

        # Left subtree
        if not self.isBST(root.left):
            return False

        # Current node check (strictly greater than prev → no duplicates allowed)
        if root.data <= self.prev:
            return False
        self.prev = root.data

        # Right subtree
        return self.isBST(root.right)


        #code here