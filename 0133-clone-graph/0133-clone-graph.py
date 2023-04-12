"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def dfs(vertix):
            if vertix in oldToNew:
                return oldToNew[vertix]
            
            copy = Node(vertix.val)
            oldToNew[vertix] = copy
            
            for neighbor in vertix.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
        
        return dfs(node) if node else None