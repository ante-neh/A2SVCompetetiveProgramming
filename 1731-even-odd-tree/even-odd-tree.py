# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        index = 0

        while queue:
            size, level = len(queue), []
            for i in range(size):
                node = queue.popleft()
                if index % 2:
                    if not level:
                        if node.val % 2:
                            return False
                        level.append(node.val)
                    else:
                        if node.val % 2 or level[-1] <= node.val:
                            return False
                        level.append(node.val)

                else:
                    if not level:
                        if not node.val % 2:
                            return False
                        level.append(node.val)
                    else:
                        if not node.val % 2 or level[-1] >= node.val:
                            return False
                        level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            index += 1

        return True


        
