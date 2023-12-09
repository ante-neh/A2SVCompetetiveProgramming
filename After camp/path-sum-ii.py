# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, cur):
            nonlocal result
            if not node:
                return

            cur.append(node.val)
            if not node.left and not node.right:
                if sum(cur) == targetSum:
                    result.append(cur[:])

            dfs(node.left, cur)
            dfs(node.right, cur)
            cur.pop()

        dfs(root, [])

        return result