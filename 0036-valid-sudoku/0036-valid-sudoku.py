class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = 9, 9 # len(board), len(board[0])
        rows, cols, cubes = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(m):
            for j in range(n):
                current = board[i][j]
                if current != ".": 
                    if current in rows[i]:
                        return False
                    else:
                        rows[i].add(current)
                    if current in cols[j]:
                        return False
                    else:
                        cols[j].add(current)
                    if current in cubes[(i//3, j//3)]:
                        return False
                    else:
                        cubes[(i//3, j//3)].add(current)
        return True