class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.connections = defaultdict(str)
        for i in range(len(s1)):
            self.connections[s1[i]] = s1[i]
            self.connections[s2[i]] = s2[i]
        
        for i in range(len(s1)):
            self.union(s1[i], s2[i])
        
        smallestEquv = []
        
        for c in baseStr:
            val = self.find(c)
            if val != "":
                smallestEquv.append(val)
            else:
                smallestEquv.append(c)
            
        return "".join(smallestEquv)
        
    def find(self, x):
        parent = self.connections[x]
        while parent != self.connections[parent]:
            parent = self.connections[parent]
        
        while x != self.connections[x]:
            nextConnector = self.connections[x]
            self.connections[x] = parent
            x = nextConnector
            
        return x
    
    def union(self, x, y):
        xrep, yrep = self.find(x), self.find(y)
        if xrep != yrep:
            if xrep < yrep:
                self.connections[yrep] = xrep
                self.update(yrep, xrep)
                
            else:
                self.connections[xrep] = yrep
                self.update(xrep, yrep)
                
    def update(self, old, new):
        for node, parent in self.connections.items():
            if parent == old:
                self.connections[node] = new

        
        