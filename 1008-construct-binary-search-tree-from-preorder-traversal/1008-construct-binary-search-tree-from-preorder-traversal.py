# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = self.dfs(preorder)
        return root
    
    
    def dfs(self, arr):
        if not arr:
            return None
        root = TreeNode(arr[0])

        right = len(arr)
        for i in range(1, len(arr)):
            if arr[i] > arr[0]:
                right = i
                break

        root.left = self.dfs(arr[1:right])
        root.right = self.dfs(arr[right:])

        return root