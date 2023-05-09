class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primarySum, secondarySum = 0, 0
        
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i - j == 0:
                    primarySum += mat[i][j]     
                if i + j == len(mat) - 1 and i != j:
                    secondarySum += mat[i][j]
                    
        return primarySum + secondarySum