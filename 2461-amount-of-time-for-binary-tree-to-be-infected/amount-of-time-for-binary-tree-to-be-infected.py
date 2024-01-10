# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        time = 0
        def dfs(node):
            nonlocal time 
            depth = 0
            if not node:
                return depth

            left = dfs(node.left)
            right = dfs(node.right)

            if node.val == start:
                time = max(left, right)
                depth -= 1

            elif left >= 0 and right >= 0:
                depth = max(left, right) + 1

            else:
                time = max(time, abs(left) + abs(right))
                depth = min(left, right) - 1


            return depth
        
        dfs(root)

        return time 