class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        def dfs(row, col):
            if (row < 0 or row >= len(grid) or 
                col < 0 or col >= len(grid[0]) or 
                grid[row][col] == 0 or ((row, col) in visited)):
                
                return 0
            visited.add((row, col))
            count = 1 + dfs(row + 1, col) + dfs(row - 1, col)+ dfs(row, col + 1) + dfs(row, col - 1)           
            return count
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not(r, c) in visited and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
                    
        return maxArea
            
            