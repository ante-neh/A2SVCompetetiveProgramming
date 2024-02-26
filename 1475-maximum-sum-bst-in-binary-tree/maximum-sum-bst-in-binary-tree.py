# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum = 0

        def dfs(node):
            if not node:
                return -inf, inf, 0, True

            lmax, lmin, lsum, lbst = dfs(node.left)
            rmax, rmin, rsum, rbst = dfs(node.right)

            if lbst and rbst and lmax < node.val < rmin:
                curSum = node.val + lsum + rsum
                self.maxSum = max(self.maxSum, curSum)
                return [max(node.val, rmax), min(node.val, lmin), curSum, True]

            return [-inf, inf, 0, False]

        dfs(root)

        return self.maxSum


