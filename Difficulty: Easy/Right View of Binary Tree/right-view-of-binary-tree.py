'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def rightView(self, root):
        if not root:
            return
        q=[root]
        result=[]
        while q:
            level_size=len(q)
            for i in range(level_size):
                node=q.pop(0)
                if i==level_size-1:
                    result.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
        # code here
        