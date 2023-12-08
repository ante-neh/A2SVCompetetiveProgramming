# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minDiff = float("inf")
        inorder = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        dfs(root)

        for i in range(1, len(inorder)):
            minDiff = min(minDiff, inorder[i] - inorder[i - 1])

        return minDiff