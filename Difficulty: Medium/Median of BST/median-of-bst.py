

class Solution:
    # Iterative inorder traversal
    def inorder(self, root):
        stack, arr = [], []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            arr.append(curr.data)   # append node value
            curr = curr.right
        return arr

    # Find median of BST
    def findMedian(self, root):
        arr = self.inorder(root)
        n = len(arr)
        if n % 2 == 0:
            # Even number of nodes: return lower middle
            mid_index = n // 2 - 1
            return arr[mid_index]
        else:
            # Odd number of nodes: return middle element
            mid_index = n // 2
            return arr[mid_index]
