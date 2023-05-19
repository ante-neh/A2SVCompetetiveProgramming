class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.connections = {i:i for i in range(len(accounts))}
        self.size = {i:1 for i in range(len(accounts))}
        result = [set() for i in range(len(accounts))]
        ans = []
        
        for i in range(len(accounts)):
            for j in range(i + 1, len(accounts)):
                for k in range(1, len(accounts[i])):
                    if accounts[i][k] in accounts[j]:
                        self.union(i, j)
        
        
        for i in range(len(accounts)):
            index = self.find(i)
            for j in range(len(accounts[i])):
                result[index].add(accounts[i][j])
                
        for i in range(len(result)):
            result[i] = sorted(result[i])
                
        for res in result:
            if len(res) != 0:
                ans.append(list(res))
        
        for i in range(len(ans)):
            first = ""
            for j in range(len(ans[i])):
                if '@' not in ans[i][j] and j != 0:
                    first = ans[i].pop(j)
                    break
                    
            if first:        
                ans[i].insert(0, first) 
                
        return ans
                        
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
        
        if xrep  != yrep:
            if self.size[xrep] > self.size[yrep]:
                self.connections[yrep] = xrep
                self.size[xrep] += self.size[yrep]
            
            else:
                self.connections[xrep] = yrep
                self.size[yrep] += self.size[xrep]