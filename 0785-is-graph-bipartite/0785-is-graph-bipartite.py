class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.colors = [0 for i in range(len(graph))]
        self.queue = deque()
        result = True
        for i in range(len(graph)):
            if self.colors[i] == 0:
                self.queue.append(i)
                self.colors[i] = 1
                if not self.bfs(graph):
                    result = False
                    
        return result
        
    def bfs(self, graph):
        while self.queue:
            node = self.queue.popleft()
            for neighbor in graph[node]:
                if self.colors[neighbor] != 0:
                    if self.colors[node] == self.colors[neighbor]:
                        return False
                else:
                    self.queue.append(neighbor)
                    self.colors[neighbor] = -1 * self.colors[node]
                
                
        return True
    
            