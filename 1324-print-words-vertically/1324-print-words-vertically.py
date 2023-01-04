class Solution:
    def printVertically(self, s: str) -> List[str]:
        def transpose(grid):
            transpose= [[0] * len(grid) for i in range(len(grid[0]))] 
            
            for c in range(len(grid[0])):
                for r in range(len(grid)):
                    transpose[c][r] = grid[r][c]
                    
            return transpose
        
        
        
        s = s.split()
        maxLen = 0
        
        for word in s:
            maxLen = max(maxLen, len(word))
            
            
            
        grid = [[" "] * maxLen for i in range(len(s))]
        
        for i in range(len(s)):
            for j in range(len(s[i])):
                grid[i][j] = s[i][j]
                
        
        transposedGrid = transpose(grid)
        modifiedString = []
        
        for i in range(len(transposedGrid)):
            curString = ""
            
            for j in range(len(transposedGrid[i])):
                curString += transposedGrid[i][j]
                
            modifiedString.append(curString.rstrip())
            
        return modifiedString