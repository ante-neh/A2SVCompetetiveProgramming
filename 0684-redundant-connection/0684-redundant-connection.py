class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connections = {i:i for i in range(1, len(edges) + 1)}
        size = [1] * (len(edges) + 1)
        for u, v in edges:
            if not self.union(connections, size, u, v):
                return [u, v]
            
    def find(self, connections, x):
        parent = connections[x]
        while parent != connections[parent]:
            parent = connections[parent]
        
        while x != connections[x]:
            connections[x] = parent
            x = connections[x]
            
        return x
    
    def union(self, connections, size, x, y):
        xrep, yrep = self.find(connections, x), self.find(connections, y)
        if xrep != yrep:
            if size[xrep] > size[yrep]:
                connections[yrep] = xrep
                size[xrep] += size[yrep]
            else:
                connections[xrep] = yrep
                size[yrep] += size[xrep]
                
            return True
        
        return False
    
        
        