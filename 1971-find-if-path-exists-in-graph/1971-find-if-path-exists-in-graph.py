class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = [False] * n
        
        def dfs(vertix):
            if vertix == destination:
                return True
            
            if not visited[vertix]:
                visited[vertix] = True
                for neighbour in graph[vertix]:
                    if dfs(neighbour):
                        return True
                    
            return False
        
        return dfs(source)