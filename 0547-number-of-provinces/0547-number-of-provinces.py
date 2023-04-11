class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        count = 0
        visited = set()
        
        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if isConnected[r][c] == 1:
                    graph[r + 1].append(c + 1)
                    graph[c + 1].append(r + 1)
                    
        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if not neighbour in visited:
                    dfs(neighbour)
                    
        
        for i in graph:
            if not i in visited:
                count += 1
                dfs(i)
                
        return count
                    
        