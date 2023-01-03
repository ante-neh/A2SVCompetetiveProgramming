class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowFreq = defaultdict(int)
        
        for row in range(len(grid)):
            rowFreq[tuple(grid[row])] += 1 
            
        numberOfPairs = 0
        
        for r in range(len(grid)):
            column = []
            for c in range(len(grid)):
                column.append(grid[c][r])
                
            numberOfPairs += rowFreq[tuple(column)]
            
        return numberOfPairs
                    
                