''' 
class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''

class Solution:
    def leftView(self, root):
        if not root:
            return []
        
        q = [root]
        result = []
        
        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.pop(0)
                
                # first node at each level (left view)
                if i == 0:
                    result.append(node.data)
                
                # add child nodes to queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return result

        # code here
        