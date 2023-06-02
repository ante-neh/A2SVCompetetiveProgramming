class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        maxNumBombs = 0
        
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                
                d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                
                if d <= r1:
                    graph[i].append(j)
                    
                if d <= r2:
                    graph[j].append(i)
                    
        
        def dfs(node,visited):
            if node in visited:
                return 0
            
            visited.add(node)
            
            for neighbor in graph[node]:
                dfs(neighbor, visited)
                
            return len(visited)
        
        for i in range(len(bombs)):
            maxNumBombs = max(maxNumBombs, dfs(i, set()))
            
        return maxNumBombs
            
        
        