class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate():
            mat.reverse()
            
            for r in range(len(mat)):
                for c in range(r + 1, len(mat)):
                    mat[r][c], mat[c][r] = mat[c][r], mat[r][c]
                    
            return mat
        
        return any(rotate() == target for _ in range(4))