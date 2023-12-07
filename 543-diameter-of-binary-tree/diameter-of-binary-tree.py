# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def dfs(node):
            nonlocal maxDiameter
            if not node:
                return 0
            
            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            maxDiameter = max(left + right - 1, maxDiameter)
            return max(left, right)

        dfs(root)

        return maxDiameter - 1