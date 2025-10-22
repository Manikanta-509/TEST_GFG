class Solution:
    def largestBst(self, root):
        self.max_size = 0
        def dfs(node):
            if not node:
                return True,float('inf'),float('-inf'),0
            l_dfs,l_min,l_max,l_size=dfs(node.left)
            r_dfs,r_min,r_max,r_size=dfs(node.right)
            if l_dfs and r_dfs and l_max<node.data<r_min:
                size=l_size+r_size+1
                self.max_size=max(self.max_size,size)
                return True,min(l_min,node.data),max(r_max,node.data),size
            return False,0,0,0
        dfs(root)
        return self.max_size
