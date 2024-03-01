class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.root = [i for i in range(n)]
        self.rank = [1] * n

        for r in range(n):
            for c in range(len(isConnected[0])):
                if isConnected[r][c] and self.find(r) != self.find(c):
                    self.union(r, c)

        numberOfProvices = 0

        for i in range(n):
            if i == self.root[i]:
                numberOfProvices += 1

        return numberOfProvices

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY

            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    