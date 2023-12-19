# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lowestCommonAncestor = None

        def dfs(node):
            nonlocal lowestCommonAncestor
            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            mid = node.val == p.val or node.val == q.val

            if mid + left + right >= 2:
                lowestCommonAncestor = node

            return left or right or mid

        dfs(root)

        return lowestCommonAncestor