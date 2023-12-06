# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            
        def dfs(node):
            if not node:
                return TreeNode(val)
            elif val < node.val:
                node.left = dfs(node.left)
                return node
            else:
                node.right = dfs(node.right)
                return node

        dfs(root)

        return root  