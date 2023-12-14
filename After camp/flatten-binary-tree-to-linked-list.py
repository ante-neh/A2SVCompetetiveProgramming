# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return [None, None]
            
            if not node.left and not node.right:
                return [node, node]

            left = dfs(node.left)
            right = dfs(node.right)

            if not left[0] and right[0]:
                node.right = right[0]
                node.left = None
                return [node, right[1]]

            if not right[0] and left[0]:
                node.right = left[0]
                node.left = None
                return [node, left[1]]
            
            node.right = left[0]
            node.left = None
            left[1].right = right[0]
            
            return [node, right[1]]

        dfs(root)
