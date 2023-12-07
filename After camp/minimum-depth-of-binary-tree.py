# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return float("inf")

            if not node.left and not node.right:
                return 1
            
            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)

            return min(right, left)

        return dfs(root) if dfs(root) != float('inf') else 0

