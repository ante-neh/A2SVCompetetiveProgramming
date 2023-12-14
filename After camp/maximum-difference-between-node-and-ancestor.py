# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [float("inf"), float("-inf"), float("-inf")]

            if not node.left and not node.right:
                return [node.val, node.val, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            dif1 = 0 if abs(node.val - left[1]) == float("inf") else abs(node.val - left[1])
            dif2 = 0 if abs(node.val - left[0]) == float("inf") else abs(node.val - left[0])
            dif3 = 0 if abs(node.val - right[1]) == float("inf") else abs(node.val - right[1])
            dif4 = 0 if abs(node.val - right[0]) == float("inf") else abs(node.val - right[0])
            maxDif = max(dif1, dif2, dif3, dif4, left[-1], right[-1])

            return [min(left[0], right[0], node.val), max(left[1], right[1], node.val ), maxDif]

        result = dfs(root)

        return result[-1]