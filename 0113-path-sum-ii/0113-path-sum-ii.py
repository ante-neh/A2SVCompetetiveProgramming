# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def pathS(node, cur):
            if not node:
                return
            
            cur.append(node.val)
            if not node.left and not node.right:
                if sum(cur) == targetSum:
                    res.append(cur[:])
                    
            pathS(node.left, cur)
            pathS(node.right, cur)
            cur.pop()
            
        pathS(root, [])
        return res