# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        maxDifference = 0
        def dfs(node):
            nonlocal maxDifference
            if not node:
                return 0

            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            maxDifference = max(abs(right - left), maxDifference)

            return max(right, left)

        dfs(root)
        
        return maxDifference <= 1