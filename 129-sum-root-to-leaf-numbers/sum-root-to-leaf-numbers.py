# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum = 0

        def dfs(node, cur):
            nonlocal sum
            if not node:
                return 
            
            if not node.left and not node.right:
                cur.append(str(node.val))
                sum += int("".join(cur))
                cur.pop()
                return
            
            cur.append(str(node.val))
            dfs(node.left, cur)
            dfs(node.right, cur)
            cur.pop()

        dfs(root, [])

        return sum 
