# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if not node:
                return [float("-inf"), float("-inf")]
            
            if not node.left and not node.right:
                return [node.val, depth]

            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)

            if left[1] == right[1]:
                return [right[0] + left[0], left[1]]
            
            elif left[1] > right[1]:
                return left

            return right

        return dfs(root, 0)[0]