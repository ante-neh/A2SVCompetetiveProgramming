class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(row, col):
            if (row < 0 or row >= len(board) or 
                col < 0 or col >= len(board[0]) or 
                board[row][col] == "X" or (row, col) in visited):
                return
            
            visited.add((row, col))
            
            for r, c in directions:
                newRow, newCol = r + row, col + c
                dfs(newRow, newCol)
                
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1) and board[row][col] == "O":
                    dfs(row, col)
                    
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "O" and not (r, c) in visited:
                    board[r][c] = "X"
                