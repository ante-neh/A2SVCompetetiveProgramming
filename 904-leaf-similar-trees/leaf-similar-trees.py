# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, result):
            if not node:
                return 

            if not node.left and not node.right:
                result.append(node.val)
            
            dfs(node.left, result)
            dfs(node.right, result)

            return result

        result1 = dfs(root1, [])
        result2 = dfs(root2, [])
        
        
        if len(result1) != len(result2):
            return False 

        for i in range(len(result1)):
            if result1[i] != result2[i]:
                return False

        return True

