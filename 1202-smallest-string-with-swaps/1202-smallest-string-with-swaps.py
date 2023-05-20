class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.connections = {i:i for i in range(len(s))}
        self.size = {i:1 for i in range(len(s))}
        graph = defaultdict(list)
        result = []
        
        for i, j in pairs:
            self.union(i, j)
            
        for i in range(len(s)):
            graph[self.find(i)].append(s[i])
        
        for item in graph.items():
            item[1].sort()
                    
        for i in range(len(self.connections)):
            result.append(graph[self.find(i)].pop(0))
            
        return "".join(result)
        
    def find(self, x):
        parent = self.connections[x]
        
        while parent != self.connections[parent]:
            parent = self.connections[parent]
            
        while x != self.connections[x]:
            nextConnections = self.connections[x]
            self.connections[x] = parent
            x = nextConnections
            
        return x
    
    
    def union(self, x, y):
        xrep, yrep = self.find(x), self.find(y)
        if xrep != yrep:
            if self.size[xrep] > self.size[yrep]:
                self.connections[yrep] = xrep
                self.size[xrep] += self.size[yrep]
            
            else:
                self.connections[xrep] = yrep
                self.size[yrep] += self.size[xrep]
        
                
            