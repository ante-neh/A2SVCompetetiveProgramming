# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return [None, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            if left[1] == right[1]:
                return [node, left[1] + 1]
            
            if left[1] > right[1]:
                left[1] += 1
                return left
            right[1] += 1
            return right

        result = dfs(root)

        return result[0]



            