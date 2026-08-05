# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # res = []
        self.counter = k
        self.res = root.val
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            # res.append(node.val)
            self.counter-=1
            if self.counter == 0:
                self.res = node.val
            inorder(node.right)
        
        
        inorder(root)
        return self.res
        # return res[k-1]
        
        