class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        oldColor = image[sr][sc]
        
        def inbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == oldColor
            
        if oldColor == color:
            return image
        
        def dfs(row, col):
            if inbound(row, col):
                image[row][col] = color
                
                for rowChange, colChange in directions:
                    newRow = row + rowChange
                    newCol = col + colChange
                    dfs(newRow, newCol)
                    
        dfs(sr, sc)
        
        return image