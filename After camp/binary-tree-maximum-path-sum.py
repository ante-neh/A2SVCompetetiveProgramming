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

            maxPath = max(maxPath, node.val + left + right, node.val, node.val + left, node.val + right)

            return max(node.val + max(left, right), node.val)

        dfs(root)

        return maxPath