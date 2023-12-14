# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.result = []
        def dfs(node, parent, depth, val):
            if not node:
                return

            if node.val == val:
                if parent:
                    self.result.append([parent.val, depth])
                else:
                    self.result.append([None, depth])
            
            dfs(node.left, node, depth + 1, val)
            dfs(node.right, node, depth + 1, val)
        
        dfs(root, None, 0, x)
        dfs(root, None, 0, y)
        
        return self.result[0][0] != self.result[1][0] and self.result[0][1] == self.result[1][1]
        



            