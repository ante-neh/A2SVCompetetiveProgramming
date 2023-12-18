# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, sum):
            if not node:
                return 

            if not node.left and not node.right:
                return sum + node.val == targetSum

            return dfs(node.left, sum + node.val) or dfs(node.right, sum + node.val)

        return dfs(root, 0)