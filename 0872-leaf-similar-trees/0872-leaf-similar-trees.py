# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1, leaves2 = [], []
        
        def findLeaf(node, cur):
            if not node:
                return
            
            if not node.left and not node.right:
                cur.append(node.val)
                
            findLeaf(node.left, cur)
            findLeaf(node.right, cur)
            
            return cur
            
        leaves1, leaves2 = findLeaf(root1, []), findLeaf(root2, [])
        
        return leaves1 == leaves2