# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True
        def dfs(node):
            nonlocal result
            if not node:
                return -1

            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)

            if abs(right - left) > 1:
                result = False
            
            return max(left, right)

        dfs(root)

        return result