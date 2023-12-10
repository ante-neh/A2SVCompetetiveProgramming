# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.sumDiffPair = defaultdict(int)
        self.sumDiffPair[0] = 1
        
        def dfs(node, cur):
            if not node:
                return

            cur += node.val
            self.count += self.sumDiffPair[cur - targetSum]
            self.sumDiffPair[cur] += 1

            dfs(node.left, cur)
            dfs(node.right, cur)

            self.sumDiffPair[cur] -= 1

        dfs(root, 0)

        return self.count