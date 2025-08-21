"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""
class Solution:
    # Function to find the minimum element in the given BST.
    def minValue(self, root):
        if root is None:
            return -1   # If the tree is empty
        
        curr = root    # Start at root
        while curr.left is not None:  # Keep moving left
            curr = curr.left
        
        return curr.data   # Return the leftmost node’s value

            
        ##Your code here