# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leftLeavesSum = 0

        def dfs(node):
            nonlocal leftLeavesSum
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val

            left = dfs(node.left)
            right = dfs(node.right)

            leftLeavesSum += left

            return 0

        dfs(root)

        return leftLeavesSum 