class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                graph[i].append(rooms[i][j])
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if not neighbor in visited:
                    dfs(neighbor)
                    
        
        count = 0
        for i in range(len(rooms)):
            if i not in visited:
                count += 1
                dfs(i)
                
        return count == 1