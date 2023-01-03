class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def transposeMatrix(row): # it takes one parameter because the matrix grid is n x n
            transpose = [[0] * row for i in range(row)]
            
            for c in range(row):
                for r in range(row):
                    transpose[c][r] = grid[r][c]
                    
            return transpose
        
        transposeGrid = transposeMatrix(len(grid))        
        numberOfPairs = 0
        
        for row in grid:
            for column in transposeGrid:
                if column == row:
                    numberOfPairs += 1
                
        return numberOfPairs