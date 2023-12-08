# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        nums1, nums2 = [], []
        def dfs(node, result):
            if not node:
                return

            dfs(node.left, result)
            result.append(node.val)
            dfs(node.right, result)

            return result

        nums1.extend(dfs(root1, [])) if root1 else []
        nums2.extend(dfs(root2, [])) if root2 else []

        p1, p2, result = 0, 0, []
        
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1

        if p1 < len(nums1):
            result.extend(nums1[p1:])
        if p2 < len(nums2):
            result.extend(nums2[p2:])

        return result