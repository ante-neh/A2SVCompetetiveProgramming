class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(row):
            if row == 0:
                return [1]
            
            newRow = [1] * (row + 1)
            prev = pascal(row - 1)
            
            for i in range(1,len(prev)):
                newRow[i] = prev[i] + prev[i - 1]
                
            return newRow
            
        return pascal(rowIndex)
            