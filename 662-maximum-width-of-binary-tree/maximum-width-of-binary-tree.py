# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([[root, 0]])
        maxDistance = 0

        while queue:
            maxDistance = max(maxDistance, queue[-1][1] - queue[0][1] + 1)
            for i in range(len(queue)):
                node, d = queue.popleft()
                if node.left:
                    queue.append([node.left, d * 2])

                if node.right:
                    queue.append([node.right, d * 2 + 1])

        return maxDistance