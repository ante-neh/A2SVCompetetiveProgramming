class ThroneInheritance:

    def __init__(self, king: str):
        self.g = defaultdict(list)
        self.k = king
        self.d = set()

    def birth(self, parent: str, child: str) -> None:
        self.g[parent].append(child)

    def death(self, name: str) -> None:
        self.d.add(name)        
    
    def dfs(self, p):
        if p not in self.d:
            self.ans.append(p)
        for nxt in self.g[p]:
            self.dfs(nxt)
    
    def getInheritanceOrder(self) -> List[str]:
        self.ans = []
        self.dfs(self.k)
        return self.ans
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()