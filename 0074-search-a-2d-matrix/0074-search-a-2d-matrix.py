class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nRows =  len(matrix)
        nCols = len(matrix[0])
        
        row = nRows-1
        col = 0
        
        while 0 <= row < nRows and 0 <= col < nCols:
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                col += 1
            else:
                row -= 1
        
        return False