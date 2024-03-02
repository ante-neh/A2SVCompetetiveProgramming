class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.root = [i for i in range(len(s))]
        self.rank = [1] * len(s)
        result = []

        rootToChar = defaultdict(list)

        for i, j in pairs:
            self.union(i, j)
            
        for i in range(len(s)):
            rootToChar[self.find(i)].append(s[i])

        for item in rootToChar.items():
            item[1].sort(reverse = True)

        for i in range(len(s)):
            result.append(rootToChar[self.find(i)].pop())

        return "".join(result)

    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
                self.rank[rootY] = self.rank[rootX]

            else:
                self.root[rootY] = rootX
                self.rank[rootX] = self.rank[rootY] 