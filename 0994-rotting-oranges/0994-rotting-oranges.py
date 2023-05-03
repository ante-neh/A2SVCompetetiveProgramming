class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        minNumberOfMinutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1
                    
        while queue and fresh:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for rowChange, colChange in directions:
                    newRow, newCol = row + rowChange, col + colChange
                    if (newRow < 0 or newRow >= len(grid) or
                        newCol < 0 or newCol >= len(grid[0]) or 
                        (newRow, newCol) in visited or grid[newRow][newCol] == 0):
                        continue

                    grid[newRow][newCol] = 2
                    queue.append((newRow, newCol))
                    visited.add((newRow, newCol))
                    fresh -= 1
            
            minNumberOfMinutes += 1
            
        return minNumberOfMinutes if fresh == 0 else -1
                