# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            left1 = node1.val == node2.val and dfs(node1.left, node2.left)
            left2 = node1.val == node2.val and dfs(node1.left, node2.right)
            right1 = node1.val == node2.val and dfs(node1.right, node2.left)
            right2 = node1.val == node2.val and dfs(node1.right, node2.right)

            return (left1 or left2) and (right1 or right2)

        return dfs(root1, root2)