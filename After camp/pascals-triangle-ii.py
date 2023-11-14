class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def findPascalsRow(row):
            if row == 0:
                return [1]

            pascal = findPascalsRow(row - 1)
            result = [1] * (len(pascal) + 1)
            for i in range(1, len(pascal)):
                result[i] = pascal[i] + pascal[i - 1]

            return result

        return findPascalsRow(rowIndex)
    