# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        evenSum = 0
        
        def dfs(node, parent, grandParent):
            nonlocal evenSum
            if not node:
                return
            
            if grandParent % 2 == 0:
                evenSum += node.val   

            grandParent, parent = parent, node.val
            dfs(node.left, parent, grandParent)
            dfs(node.right, parent, grandParent)
    
        dfs(root, -1, -1)
        return evenSum
            
            
            
            

        
            
            