class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()        
        def dfs(row, col):
            if row >= len(grid) or col >= len(grid[0]) or col < 0 or row < 0 or grid[row][col] == 0:
                return 1
            
            if (row, col) in visited:
                return 0
            visited.add((row, col))
            perimeter = dfs(row, col + 1)
            perimeter += dfs(row, col - 1)
            perimeter += dfs(row + 1, col)
            perimeter += dfs(row - 1, col)
            
            return perimeter
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return dfs(r, c)
                    
        
                    
                
                