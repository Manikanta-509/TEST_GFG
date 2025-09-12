class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root, arr):
        if not root:
            return
        self.inorder(root.left, arr)
        arr.append(root.data)
        self.inorder(root.right, arr)

    def merge(self, root1, root2):
        # Step 1: get inorder traversal of both BSTs
        arr1, arr2 = [], []
        self.inorder(root1, arr1)
        self.inorder(root2, arr2)

        # Step 2: merge two sorted arrays
        i = j = 0
        merged = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        
        while i < len(arr1):
            merged.append(arr1[i])
            i += 1
        while j < len(arr2):
            merged.append(arr2[j])
            j += 1
        
        return merged
