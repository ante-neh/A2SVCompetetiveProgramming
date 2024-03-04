class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        visited = set()
        self.root = {}
        result = []

        for dividend, divisor in equations:
            visited.add(dividend)
            visited.add(divisor)
            self.root[dividend] = (dividend, 1)
            self.root[divisor] = (divisor, 1)
        
        for i, equation in enumerate(equations):
            self.union(equation[0], equation[1], values[i])

        for query in queries:
            if query[0] in visited and query[1] in visited:
                rootX = self.find(query[0])
                rootY = self.find(query[1])
                if rootX[0] != rootY[0]:
                    result.append(-1.0)
                else:
                    result.append(rootX[1] / rootY[1] )
            else:
                result.append(-1.0)

        return result

    def find(self, x):
        groupId, nodeWeight = self.root[x]
        if x != groupId:
            head, weight = self.find(groupId)
            self.root[x] = (head, weight * nodeWeight)

        return self.root[x]

    def union(self, dividend, divisor, weight):
        headDd, weightDd = self.find(dividend)
        headDv, weightDv = self.find(divisor)

        if headDd != headDv:
            self.root[headDd] = (headDv, (weight * weightDv) / weightDd)
