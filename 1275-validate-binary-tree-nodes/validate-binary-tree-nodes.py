class TreeNode:
    def __init__(self, value = 0, left = None, right = None ):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        children = set(leftChild) | set(rightChild)
        root = -1

        for i in range(n):
            if i not in children:
                root = i
                break
        
        if root == -1:
            return False

        stack = [root]
        visited = {root}

        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in visited:
                        return False
                    visited.add(child)
                    stack.append(child)

        return len(visited) == n