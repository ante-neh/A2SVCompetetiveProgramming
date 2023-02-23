class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (cols + 1) for i in range(rows + 1)]
        
        for r in range(rows):
            prefixSum = 0
            for c in range(cols):
                prefixSum += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r+1][c+1] = above + prefixSum
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.sumMat[r2][c2]
        bottomLeft = self.sumMat[r2][c1 - 1]
        topLeft = self.sumMat[r1 - 1][c1 - 1]
        topRight = self.sumMat[r1 - 1][c2]
        
        return bottomRight + topLeft - bottomLeft - topRight
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)