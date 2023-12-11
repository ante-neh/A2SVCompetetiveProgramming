# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return

        root = TreeNode(preorder.pop(0))
        postorder.pop(-1)

        if preorder:
            index = postorder.index(preorder[0])
            root.left = self.constructFromPrePost(preorder[:index + 1], postorder[:index + 1])
            root.right = self.constructFromPrePost(preorder[index + 1:], postorder[index + 1:])

        return root