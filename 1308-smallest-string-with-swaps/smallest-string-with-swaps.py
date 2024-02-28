class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        graph = defaultdict(list)
        lexicographicallySmallest = []

        for i, j in pairs:
            self.union(i, j)

        for i in range(n):
            graph[self.find(i)].append(s[i])

        for item in graph.items():
            item[1].sort()

        for i in range(n):
            lexicographicallySmallest.append(graph[self.find(i)].pop(0))
        
        return "".join(lexicographicallySmallest)

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]

        return x

    def union(self, x, y):
        xrep, yrep = self.find(x), self.find(y)
        if xrep != yrep:
            if self.rank[xrep] > self.rank[yrep]:
                self.root[yrep] = xrep
            elif self.rank[yrep] > self.rank[xrep]:
                self.root[xrep] = yrep
            else:
                self.root[yrep] = xrep
                self.rank[xrep] += 1
                
            