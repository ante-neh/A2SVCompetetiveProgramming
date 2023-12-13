class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def check(row, col):
            for i in range(len(mat[0])):
                if i != col and mat[row][i] == 1:
                    return False

            for j in range(len(mat)):
                if j != row and mat[j][col] == 1:
                    return False

            return True

        specialPositions = 0

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1 and check(r, c):
                    specialPositions += 1

        return specialPositions
