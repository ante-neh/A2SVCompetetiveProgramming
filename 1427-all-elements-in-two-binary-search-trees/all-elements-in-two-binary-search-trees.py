# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        nums = []
        def dfs(node, result):
            if not node:
                return

            dfs(node.left, result)
            result.append(node.val)
            dfs(node.right, result)

            return result

        nums.extend(dfs(root1, [])) if root1 else []
        nums.extend(dfs(root2, [])) if root2 else []
        nums.sort()

        return nums 
