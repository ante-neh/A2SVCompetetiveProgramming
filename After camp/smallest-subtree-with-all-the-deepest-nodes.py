# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.deepest = None

        def dfs(node):
            if not node:
                return [-1, None]

            if not node.left and not node.right:
                return [0, node]

            left = dfs(node.left)
            right = dfs(node.right)

            if left[0] == right[0] and left[1] and right[1]:
                return [left[0] + 1, node]
            
            if left[0] > right[0]:
                return [left[0] + 1, left[1]]
            
            return [right[0] + 1, right[1]]

        result = dfs(root)

        return result[1]
            