class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for v, u in dislikes:
            graph[v].append(u)
            graph[u].append(v)
            
        visited = [0 for _ in range(n + 1)]
        color = [0 for _ in range(n + 1)]
        
        def dfs(visited, color, node):
            for neighbor in graph[node]:
                if visited[neighbor] == False:
                    visited[neighbor] = True
                    color[neighbor] = not color[node]
                    
                    if not dfs(visited, color, neighbor):
                        return False
                    
                elif color[node] == color[neighbor]:
                    return False
                
            return True
                
        for i in range(1, n + 1):
            if visited[i] == False:
                if not dfs(visited, color,i):
                    return False
                
        return True
        
            
            
        
            