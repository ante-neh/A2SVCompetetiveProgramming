class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        queue = deque()
        ancestors = [set() for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        for index, count in enumerate(indegree):
            if count == 0:
                queue.append(index)
                
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                ancestors[neighbor].add(node)
                ancestors[neighbor].update(ancestors[node])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        for i in range(len(ancestors)):
            ancestors[i] = sorted(ancestors[i])  
        return ancestors
        
