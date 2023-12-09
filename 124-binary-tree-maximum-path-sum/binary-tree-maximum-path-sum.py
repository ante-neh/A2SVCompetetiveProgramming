# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = float("-inf")

        def dfs(node):
            nonlocal maxPath
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            maxPath = max(maxPath, max(left, 0) + max(right, 0) + node.val)

            return node.val + max(max(left, 0), max(0, right))

        dfs(root)

        return maxPath
        