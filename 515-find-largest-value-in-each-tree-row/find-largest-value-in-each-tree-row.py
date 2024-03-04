# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        largestValuesInRow = []
        queue = deque([root])

        if not root:
            return largestValuesInRow

        while queue:
            maxVal = float("-inf")
            for i in range(len(queue)):
                node = queue.popleft()
                maxVal = max(maxVal, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            largestValuesInRow.append(maxVal)

        return largestValuesInRow