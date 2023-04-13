# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def diameter(root):
            nonlocal maxDiameter
            if not root:
                return -1
            
            left = diameter(root.left)
            right = diameter(root.right)
            maxDiameter = max(maxDiameter, 2 + left + right)
            
            return 1 + max(left, right)
        
        diameter(root)
        
        return maxDiameter