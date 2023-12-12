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
                return 
            if (node.val <= p.val and node.val >= q.val) or (node.val >= p.val and node.val <= q.val):
                lowestCommonAncestor = node
                return 

            if node.val > p.val and node.val > p.val:
                dfs(node.left)

            if node.val < p.val and node.val < p.val:
                dfs(node.right)

            

        dfs(root)

        return lowestCommonAncestor