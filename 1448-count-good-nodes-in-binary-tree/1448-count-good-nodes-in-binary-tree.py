# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        numGoodNodes = 0
        def countGoodNodes(root, curMax):
            nonlocal numGoodNodes
            if not root:
                return
            
            if root.val >= curMax:
                numGoodNodes += 1
            countGoodNodes(root.left, max(curMax, root.val))
            countGoodNodes(root.right, max(curMax, root.val))
            
        countGoodNodes(root, root.val)
        
        return numGoodNodes