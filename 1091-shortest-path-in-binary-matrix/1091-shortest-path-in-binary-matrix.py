class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        visited = set()
        queue = deque([(0, 0)])
        visited.add((0, 0))
        shortestPath = 0
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        is_valid = lambda i, j: 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 0
        
        while queue:
            shortestPath += 1
            for i in range(len(queue)):
                row, col = queue.popleft()
                if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
                    return shortestPath
                for r, c in directions:
                    newRow, newCol = row + r, col + c
                    if is_valid(newRow, newCol) and (newRow, newCol) not in visited:
                        visited.add((newRow, newCol))
                        queue.append((newRow, newCol))
                    
        return -1