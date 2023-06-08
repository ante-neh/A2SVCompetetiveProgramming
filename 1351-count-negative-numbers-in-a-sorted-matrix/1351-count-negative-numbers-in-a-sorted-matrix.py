class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] < 0:
                    count += 1
                    
        return count