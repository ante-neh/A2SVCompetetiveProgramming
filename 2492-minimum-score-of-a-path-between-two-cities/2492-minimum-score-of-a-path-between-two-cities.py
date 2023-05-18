class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        connections = {i:i for i in range(1, n + 1)}
        size = {i:1 for i in range(n + 1)}
        minimum = {i:float("inf") for i in range(n + 1)}
        
        for i in range(len(roads)):
            self.union(size, connections, minimum, i, roads)
            
        oneRep = self.find(connections, 1)
        
        return minimum[oneRep]
    
    def find(self, connections,  x):
        parent = connections[x]
        while parent != connections[parent]:
            parent = connections[parent]
            
        while x != connections[x]:
            connections[x] = parent
            x = connections[x]
            
        return x
    
    def union(self, size, connections, minimum, i, roads):
        xrep, yrep = self.find(connections, roads[i][0]), self.find(connections, roads[i][1])
        if xrep != yrep:
            if size[xrep] > size[yrep]:
                connections[yrep] = xrep
                size[xrep] += size[yrep]
                minimum[xrep] = min(minimum[xrep], minimum[yrep], roads[i][2])
            else:
                connections[xrep] = yrep
                size[yrep] += size[xrep]
                minimum[yrep] = min(minimum[xrep], minimum[yrep], roads[i][2])
        
        else:
            minimum[xrep] = min(minimum[xrep], minimum[yrep], roads[i][2])
            minimum[yrep] = min(minimum[xrep], minimum[yrep], roads[i][2])
        
        
        