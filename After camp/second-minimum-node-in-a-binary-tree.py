# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        minValue = root.val
        ans = float("inf")

        def dfs(node):
            nonlocal minValue
            nonlocal ans
            if node:
                if minValue < node.val < ans:
                    ans = node.val
                elif node.val == minValue:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)

        return ans if ans != float("inf") else - 1
            