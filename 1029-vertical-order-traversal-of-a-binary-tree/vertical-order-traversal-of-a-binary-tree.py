# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columnToNode = defaultdict(list)
        verticalLevel = []
        def dfs(node, col, row):
            if not node:
                return 
            
            columnToNode[col].append([node.val, row])
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)

        dfs(root, 0, 0)
        order = list(columnToNode.keys())
        order.sort()

        for ord in order:
            nums = columnToNode[ord]
            nums.sort(key = lambda x:(x[1], x[0]))
            res = []
            for n, v in nums:
                res.append(n)
            verticalLevel.append(res)

        return verticalLevel

