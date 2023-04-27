class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        minNumberOfMinutes = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
                    
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and fresh:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for r, c in directions:
                    newRow, newCol = row + r, col + c
                    if (newRow < 0 or newRow >= len(grid) or 
                        newCol < 0 or newCol >= len(grid[0]) or 
                        grid[newRow][newCol] == 0 or grid[newRow][newCol] == 2):
                        continue
                    
                    grid[newRow][newCol] = 2
                    queue.append((newRow, newCol))
                    fresh -= 1
                    
            minNumberOfMinutes += 1
                
        return minNumberOfMinutes if fresh == 0 else -1
                    
                    
                    
        
        