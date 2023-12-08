# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minDiff = float("inf")
        prev = None

        def dfs(node):
            nonlocal prev
            nonlocal minDiff

            if not node:
                return 

            dfs(node.left)
            if prev is not None:
                minDiff = min(minDiff, node.val - prev.val)

            prev = node
            dfs(node.right)

        dfs(root)

        return minDiff

            