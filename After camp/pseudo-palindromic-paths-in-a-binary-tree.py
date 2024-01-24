# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(node, nodeFreq):
            nonlocal count
            if not node:
                return

            nodeFreq[node.val] += 1
            if not node.left and not node.right:
                c = 0
                for item in nodeFreq.items():
                    if item[1] % 2 != 0:
                        c += 1

                if c < 2:
                    count += 1
                nodeFreq[node.val] -= 1
                return

            dfs(node.left, nodeFreq)
            dfs(node.right, nodeFreq)
            nodeFreq[node.val] -= 1

        dfs(root, defaultdict(int))

        return count
