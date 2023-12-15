# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        reference = None
        def dfs(node):
            nonlocal reference
            if not node:
                return
            
            if node.val == target.val:
                reference = node
                
            dfs(node.left)
            dfs(node.right)

        dfs(cloned)

        return reference
