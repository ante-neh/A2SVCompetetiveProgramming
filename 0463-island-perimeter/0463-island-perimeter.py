class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                count = 0
                if grid[r][c] == 1:
                    if r - 1 >= 0 and grid[r - 1][c] == 1:
                        count += 1
                    if r + 1 < rows and grid[r + 1][c] == 1:
                        count += 1

                    if c - 1 >= 0 and grid[r][c - 1] == 1:
                        count += 1

                    if c + 1 < cols and grid[r][c + 1] == 1:
                        count += 1
                    perimeter += (4 - count)
                    
        return perimeter
                    
                
                