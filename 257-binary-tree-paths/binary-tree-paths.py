# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node, cur):
            nonlocal result
            if not node:
                return

            cur.append(str(node.val))
            if not node.left and not node.right:
                copy = cur[:]
                result.append("->".join(copy))

            dfs(node.left, cur)
            dfs(node.right, cur)
            cur.pop()

        dfs(root, [])
        return result