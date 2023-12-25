# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = self.dfs(root, deque())

    def dfs(self, node, inorder):
        if not node:
            return
        
        self.dfs(node.left, inorder)
        inorder.append(node.val)
        self.dfs(node.right, inorder)

        return inorder

    def next(self) -> int:
        nextNode = self.inorder.popleft()
        return nextNode

    def hasNext(self) -> bool:
        return len(self.inorder) >= 1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()