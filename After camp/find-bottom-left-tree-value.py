# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        leftMostValue = [0, root.val]

        def dfs(node, depth):
            nonlocal leftMostValue
            if not node:
                return [float("-inf"), None]
                
            if not node.left and not node.right:
                return [depth, node.val]

            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)

            if leftMostValue[0] < left[0]:
                leftMostValue[1] = left[1]
                leftMostValue[0] = left[0]
            
            if leftMostValue[0] < right[0]:
                leftMostValue[1] = right[1]
                leftMostValue[0] = right[0]

            return [depth, node.val]

        dfs(root, 0)

        return leftMostValue[1]

