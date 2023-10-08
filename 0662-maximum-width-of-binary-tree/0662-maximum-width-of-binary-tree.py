# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([([root],[1])])
        ans = 1
        while queue:
            q,i = [],[]
            cur_lv = queue.popleft()
            for cur,index in zip(cur_lv[0],cur_lv[1]):
                if cur.left:
                    q.append(cur.left)
                    i.append(2*index)
                if cur.right:
                    q.append(cur.right)
                    i.append(2*index+1)
            if q:
                ans = max(ans,i[-1]-i[0]+1)
                queue = deque([(q,i)])
                continue
            queue.clear()
        return ans
        