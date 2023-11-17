class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        def pascal(row):
            if row == 1:
                return [1]
            
            prev = pascal(row - 1)
            newRow = [1] * (len(prev) + 1)
            
            for i in range(1,len(prev)):
                newRow[i] = prev[i] + prev[i - 1]
                
            res.append(newRow)
            
            return newRow
        
        pascal(numRows)
        
        return res