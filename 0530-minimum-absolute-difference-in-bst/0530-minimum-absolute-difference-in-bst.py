# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorderNodes = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            inorderNodes.append(node.val)
            inorder(node.right)
        
        inorder(root)
        minDifference = 1e9
        for i in range(1, len(inorderNodes)):
            minDifference = min(minDifference, inorderNodes[i] - inorderNodes[i-1])

        return minDifference
        