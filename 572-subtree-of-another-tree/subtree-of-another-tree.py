# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False

            return node1.val == node2.val and isIdentical(node1.left, node2.left) and isIdentical(node1.right, node2.right)

        result = False
        def dfs(node):
            nonlocal result
            if not node:
                return

            if isIdentical(node, subRoot):
                result = True

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return result

            
            