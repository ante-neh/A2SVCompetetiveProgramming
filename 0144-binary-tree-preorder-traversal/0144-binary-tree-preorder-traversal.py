# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.left
                
            cur = stack.pop()
            cur = cur.right
            
        return res