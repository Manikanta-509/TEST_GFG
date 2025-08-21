class Solution:
    def largestBst(self, root):
        self.max_size = 0

        def dfs(node):
            if node is None:
                # For null nodes: it's a valid BST with size 0
                return True, 0, float('inf'), float('-inf')
            
            # Recursively check left and right subtrees
            l_bst, l_size, l_min, l_max = dfs(node.left)
            r_bst, r_size, r_min, r_max = dfs(node.right)

            # Check if current subtree is BST
            if l_bst and r_bst and l_max < node.data < r_min:
                size = l_size + r_size + 1
                self.max_size = max(self.max_size, size)
                return True, size, min(l_min, node.data), max(r_max, node.data)
            
            # If not BST, return False
            return False, 0, 0, 0

        dfs(root)
        return self.max_size
