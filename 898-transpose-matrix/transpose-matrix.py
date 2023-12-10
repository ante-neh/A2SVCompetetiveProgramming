class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposedMatrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                transposedMatrix[c][r] = matrix[r][c]

        return transposedMatrix