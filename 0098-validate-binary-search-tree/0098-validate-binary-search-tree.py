# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.f(root,-float('inf'), float('inf'))
    
    def f(self,node,l,h):
        return (node is None) or ((l<node.val<h) and self.f(node.left, l, node.val) and self.f(node.right, node.val, h))