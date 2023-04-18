# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # if root and root.val == targetSum and (root.right or root.left) or not root:
        #     return False
        
        def pathSum(root, curSum):
            if root:
                curSum += root.val
            if root and (root.left == None and root.right == None):
                return curSum == targetSum
            if not root:
                return False
            
            if pathSum(root.left, curSum):
                return True
            if pathSum(root.right, curSum):
                return True
            
        return pathSum(root, 0)