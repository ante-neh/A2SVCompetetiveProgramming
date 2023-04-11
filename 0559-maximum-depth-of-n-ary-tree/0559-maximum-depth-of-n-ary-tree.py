"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        max_depth = 0
        def dfs(node):
            nonlocal max_depth
            if not node.children:
                return 1
            
            max_depth = 0
            for child in node.children:
                max_depth = max(max_depth, dfs(child))
                
            return max_depth + 1
        
        return dfs(root)