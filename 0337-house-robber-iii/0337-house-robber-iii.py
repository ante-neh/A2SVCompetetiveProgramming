# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def house(node):
            if not node:
                return [0, 0]
            
            leftPair = house(node.left)
            rightPair = house(node.right)
            withNode = node.val + leftPair[1] + rightPair[1]
            withOutNode = max(leftPair) + max(rightPair)
            
            return [withNode, withOutNode]
        
        return max(house(root))
        
            
        