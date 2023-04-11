class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0
        
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
                return 
            
            visited.add((row, col))
            
            for rC, cC in directions:
                newRow, newCol = rC + row, cC + col
                if not (newRow, newCol) in visited:
                    dfs(newRow, newCol)
                    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not (r, c) in visited and (grid[r][c] == "1"):
                    count += 1
                    dfs(r, c)
                    
        return count
        