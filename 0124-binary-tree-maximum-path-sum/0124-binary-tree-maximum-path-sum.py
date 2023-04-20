# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathSum = float("-inf")
        
        def pathSum(node):
            nonlocal maxPathSum
            if not node:
                return 0
            
            left = pathSum(node.left)
            right = pathSum(node.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)
            
            maxPathSum = max(maxPathSum, node.val + leftMax + rightMax)
            
            return node.val + max(leftMax, rightMax)
        
        pathSum(root)
        
        return maxPathSum
        