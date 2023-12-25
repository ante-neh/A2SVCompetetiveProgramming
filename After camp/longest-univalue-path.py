# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.length = 0

        def dfs(node):
            if not node:
                return [0, float("inf")]

            left = dfs(node.left)
            right = dfs(node.right)

            if left[-1] == node.val and node.val == right[-1]:
                self.length = max(self.length, 2 + left[0] + right[0])
                return [1 + max(left[0], right[0]), node.val]
            elif left[-1] == node.val:
                self.length = max(self.length, left[0] + 1)
                return [left[0] + 1, node.val]

            elif right[-1] == node.val:
                self.length = max(self.length, right[0] + 1)
                return [right[0] + 1, node.val]

            return [0, node.val]

        dfs(root)

        return self.length