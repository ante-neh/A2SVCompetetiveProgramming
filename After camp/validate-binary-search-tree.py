# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        validate = True
        def dfs(node):
            nonlocal validate
            if not node:
                return 

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                if node.val <= left[0] or node.val <= left[1] or node.val >= right[0] or node.val >= right[1]:
                    validate = False

                return [min(left[0], right[0], node.val), max(left[1], right[1], node.val)]

            elif left:
                if node.val <= left[0] or node.val <= left[1]:
                    validate = False
                
                return [min(node.val, left[0]), max(node.val, left[1])]
            
            elif right:
                if node.val >= right[0] or node.val >= right[1]:
                    validate = False

                return [min(node.val, right[0]), max(node.val, right[1])]

            else:
                return [node.val, node.val]

        dfs(root)

        return validate

