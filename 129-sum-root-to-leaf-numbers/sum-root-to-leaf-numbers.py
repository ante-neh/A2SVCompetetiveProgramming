# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        totalSum = 0

        def dfs(node, cur):
            nonlocal totalSum
            if not node:
                return

            cur.append(str(node.val))
            if not node.left and not node.right:
                totalSum += int("".join(cur))
                cur.pop()
                return 

            dfs(node.left, cur)
            dfs(node.right, cur)
            cur.pop()

        dfs(root, [])

        return totalSum