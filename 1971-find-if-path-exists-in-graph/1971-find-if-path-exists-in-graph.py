class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        connections = {i:i for i in range(n)}
        size = [1] * n
        for u, v in edges:
            self.union(connections, size, u, v)
            
        return self.connencted(connections, source, destination)
    
    def find(self, connections, x):
        parent = connections[x]
        while parent != connections[parent]:
            parent = connections[parent]
        
        while x != connections[x]:
            connections[x] = connections[parent]
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
                
    def connencted(self,connections, x, y):
        return self.find(connections, x) == self.find(connections, y)