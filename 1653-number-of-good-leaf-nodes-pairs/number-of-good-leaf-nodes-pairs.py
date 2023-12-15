# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0

        def dfs(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [1]

            left = dfs(node.left)
            right = dfs(node.right)

            for i in left:
                if i >= distance:
                    continue
                
                for j in right:
                    if i + j <= distance:
                        self.count += 1

            return [i + 1 for i in left + right]

        dfs(root)

        return self.count 
            

             