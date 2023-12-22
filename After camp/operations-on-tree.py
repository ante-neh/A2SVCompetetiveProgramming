class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.graph = defaultdict(list)
        self.state = [None for i in range(len(parent))]

        for i in range(len(parent)):
            self.graph[parent[i]].append(i)


    def lock(self, num: int, user: int) -> bool:
        if self.state[num]:
            return False

        self.state[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.state[num] == user:
            self.state[num] = None
            return True
        
        return False

    def upgrade(self, num: int, user: int) -> bool:
        i = num

        while i != -1:
            if self.state[i]:
                return False
            i = self.parent[i]
        
        lockedCount = 0
        queue = deque([num])

        while queue:
            node = queue.popleft()
            if self.state[node]:
                self.state[node] = None
                lockedCount += 1
            queue.extend(self.graph[node])

        if lockedCount > 0:
            self.state[num] = user
            return True
        
        return False

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)