# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self, root, k):
        self.count = 0
        self.result = -1

        def reverseInorder(node):
            if not node or self.count >= k:
                return

            # Step 1: Go right first
            reverseInorder(node.right)

            # Step 2: Visit this node
            self.count += 1
            if self.count == k:
                self.result = node.data
                return

            # Step 3: Then go left
            reverseInorder(node.left)

        reverseInorder(root)
        return self.result

        #your code here