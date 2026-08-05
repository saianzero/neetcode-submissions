# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node,lv, rv):
            if not node:
                return True
            if not ( lv < node.val < rv):
                return False
            
            left = valid(node.left, lv, node.val)
            right = valid(node.right, node.val, rv)

            return left and right
        return valid(root, float("-inf"), float("inf"))
        
