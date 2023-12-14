# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def dfs(node, low, high):
            if not node:
                return

            self.max = max(self.max, abs(node.val - low), abs(node.val - high))
            dfs(node.left, min(node.val, low), max(node.val, high))
            dfs(node.right, min(node.val, low), max(node.val, high))

        dfs(root, root.val, root.val)

        return self.max
