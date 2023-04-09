"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        def f(root):
            if not root.children: return 1
            h = -1
            for v in root.children:
                h = max(h, f(v))
            return 1 + h
        return f(root)