class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        self.connections ={}
        self.size = {}
        for equation in equations:
            self.connections[equation[0]] = equation[0]
            self.size[equation[0]] = 1
            self.connections[equation[-1]] = equation[-1]
            self.size[equation[-1]] = 1
            
        for equation in equations:
            sign = equation[1:-1]
            if sign == "==":
                self.union(equation[0], equation[-1])
            
        satisfied = True
        for equation in equations:
            val1, val2 = self.find(equation[0]), self.find(equation[-1])
            sign = equation[1:-1]
            
            if sign == "==" and val1 != val2:
                satisfied = False
            elif sign == "!=" and val1 == val2:
                satisfied = False
        
        return satisfied
            
    def find(self, x):
        parent = self.connections[x]
        while parent != self.connections[parent]:
            parent = self.connections[parent]
        
        while x != self.connections[x]:
            nextConnection = self.connections[x]
            self.connections[x] = parent
            x = nextConnection
            
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
                
            