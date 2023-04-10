class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        oldColor = image[sr][sc]
        
        if oldColor == color:
            return image
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or image[row][col] != oldColor:
                return 
            
            image[row][col] = color
            
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            
        dfs(sr, sc)
        return image
                