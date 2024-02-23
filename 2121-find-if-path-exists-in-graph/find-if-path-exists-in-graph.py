class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        queue = deque([source])
        visited = set()
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            
            for neighbor in graph[node]:
                if not neighbor in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    
        return False