# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def dfs(node, cur):
            if not node:
                return

            cur[node.val] += 1
            if not node.left and not node.right:
                countPartiy = 0
                for val in cur.values():
                    if val % 2 == 1:
                        countPartiy += 1
                        
                if countPartiy < 2:
                    self.count += 1

                cur[node.val] -= 1
                return 

            dfs(node.left, cur)
            dfs(node.right, cur)
            cur[node.val] -= 1

        dfs(root, defaultdict(int))

        return self.count

