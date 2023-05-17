class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
        1: [(0, -1), (0, 1)],   # Left, Right
        2: [(-1, 0), (1, 0)],   # Up, Down
        3: [(0, -1), (1, 0)],    # Left, Down
        4: [(0, 1), (1, 0)],     # Right, Down
        5: [(0, -1), (-1, 0)],   # Left, Up
        6: [(0, 1), (-1, 0)]     # Right, Up
        }

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(row, col):
            if row == m - 1 and col == n - 1:
                return True

            visited[row][col] = True
            street_type = grid[row][col]

            for dx, dy in directions[street_type]:
                next_row, next_col = row + dx, col + dy

                if next_row >= 0 and next_row < m and next_col >= 0 and next_col < n and not visited[next_row][next_col]:
                    next_street_type = grid[next_row][next_col]
                    # Check if the next street segment connects to the current one
                    if (-dx, -dy) in directions[next_street_type]:
                        if dfs(next_row, next_col):
                            return True

            return False

        return dfs(0, 0)








            
            