# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        def dfs(root):
            if not root:
                return []
            left = dfs(root.left)
            right = dfs(root.right)
            x = [root.val]
            for i in left:
                x.append(root.val+i)
            for j in right:
                x.append(root.val+j)
            self.count += x.count(targetSum)
            return x
        dfs(root)
        return self.count