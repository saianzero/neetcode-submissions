# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # largest =  float("-inf")
        self.count = 0
        def dfs(node, largest):

            if not node:
                return 

            if node.val >= largest:
                self.count+=1

            largest = max(largest, node.val)

            dfs(node.left, largest)
            dfs(node.right,largest)
        
        dfs(root, float("-inf"))
        return self.count


    