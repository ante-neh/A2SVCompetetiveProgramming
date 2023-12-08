# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        result = []

        def dfs(node):
            nonlocal result
            if not node:
                return
            
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        result.sort()
        for i in range(1, len(result)):
            if result[i] != result[i - 1]:
                return result[i]

        return -1