# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([[root, 0]])
        maxLength = 0

        if not root:
            return maxLength

        while queue:
            cur, start = queue[0]       #[node, position]
            for i in range(len(queue)):
                node, end = queue.popleft() #[node, position]
                if node.left:
                    queue.append([node.left, end * 2])
                if node.right:
                    queue.append([node.right, end * 2 + 1])

            maxLength = max(maxLength, end - start + 1)

        return maxLength