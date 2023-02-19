class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        for rows in grid:
            rows.sort()
            
        m, n = len(grid), len(grid[0])
        for j in range(n-1, -1, -1):
            temp_max = -float('inf')
            for i in range(m):
                temp_max = max(temp_max, grid[i][j])
                
            ans += temp_max
            
        return ans