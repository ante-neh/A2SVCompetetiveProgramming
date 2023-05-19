class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        self.connections = {i:i for i in range(len(stones))}
        self.size = {i:1 for i in range(len(stones))}
        numStonesRemain = 0
        
        
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0]:
                    self.union(i, j)
                elif stones[i][1] == stones[j][1]:
                    self.union(i, j)
        
        for i in range(len(stones)):
            if self.find(i) != i:
                numStonesRemain += 1
                
        return numStonesRemain
        
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
                    
    