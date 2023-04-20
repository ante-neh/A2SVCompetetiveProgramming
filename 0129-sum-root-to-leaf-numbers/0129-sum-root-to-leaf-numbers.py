# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        pathSum = 0
        def sumRootToLeaf(node, curSum):
            nonlocal pathSum
            if not node:
                return 
            
            curSum.append(str(node.val))
            if not node.left and not node.right:
                pathSum += int("".join(curSum))
                
            sumRootToLeaf(node.left, curSum)
            sumRootToLeaf(node.right, curSum)
            curSum.pop()
            
        sumRootToLeaf(root, [])
        
        return pathSum