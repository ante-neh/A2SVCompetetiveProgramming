class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()
        visited.add(0)
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in rooms[node]:
                    if not neighbor in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        
        return len(rooms) == len(visited)
        