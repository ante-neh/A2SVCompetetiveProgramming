class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (len(mat) * len(mat[0])) != r * c:
            return mat
        
        oneDMat =[0] * (len(mat) * len(mat[0]))
        col = len(mat[0])
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                oneDMat[(i * col) + j] = mat[i][j]
                
        reshaped = [[0] * c for _ in range(r)]
        
        for i in range(len(oneDMat)):
            reshaped[i//c][i % c] = oneDMat[i]

        return reshaped
                        