class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connections = {i:i for i in range(len(isConnected))}
        size = [1] * len(isConnected)
        
        for r in range(len(isConnected)):
            for c in range(len(isConnected[r])):
                if isConnected[r][c] == 1:
                    if self.find(connections, r) != self.find(connections, c):
                        self.union(connections, size, r, c)
        
        return self.count(connections)
        
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
                self.update_connections(connections, yrep, xrep)
            else:
                connections[xrep] = yrep
                size[yrep] += size[xrep]
                self.update_connections(connections, xrep, yrep)

    def update_connections(self, connections, old_rep, new_rep):
        for node, parent in connections.items():
            if parent == old_rep:
                connections[node] = new_rep
                
    def count(self, connections):
        count = set()
        for item in connections.items():
            count.add(item[1])
            
        return len(count)
                
        
                    
                    
        