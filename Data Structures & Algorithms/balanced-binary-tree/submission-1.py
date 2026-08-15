class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        if not root:
            return self.res
        
        def dfs(root):
            if not root:
                return 0
            
            hl = dfs(root.left)
            hr = dfs(root.right)
            if abs(hl - hr) > 1:
                self.res = False

            return 1 + max(hl, hr)
        dfs(root)
        return self.res