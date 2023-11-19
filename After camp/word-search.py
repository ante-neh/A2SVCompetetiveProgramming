class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def backtrack(row, col , index):
            if index == len(word):
                return True

            if (row < 0 or row >= len(board) or 
            col < 0 or col >= len(board[0]) or 
            (row, col) in visited or word[index] != board[row][col]):
                return False


            visited.add((row, col))
            for R, C in directions:
                r, c = row + R, col + C
                if backtrack(r, c, index + 1):
                    return True

            visited.remove((row, col))
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True

        return False 