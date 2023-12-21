# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.nodeToSubTree = defaultdict(int)
        self.duplicate = []

        def dfs(node):
            if not node:
                return ''

            encoded = str(node.val) + "#" + dfs(node.left) + "#" + dfs(node.right)
            self.nodeToSubTree[encoded] += 1

            if self.nodeToSubTree[encoded] == 2:
                self.duplicate.append(node)

            return encoded

        dfs(root)

        return self.duplicate