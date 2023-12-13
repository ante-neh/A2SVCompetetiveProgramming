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
        if not root:
            return 

        preorder = []
        def dfs(node):
            if not node:
                return
            
            preorder.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        preorder.pop(0)
        index = 0
        def build(node):
            nonlocal index
            if index >= len(preorder):
                return

            node.right = TreeNode(preorder[index])
            node.left = None

            index += 1
            build(node.right)

        build(root)

