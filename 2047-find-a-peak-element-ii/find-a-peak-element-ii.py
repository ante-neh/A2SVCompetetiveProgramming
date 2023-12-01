class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def binarySearch(i, row):
            left, right = 0, len(row)

            while left + 1 < right:
                mid = left + (right - left) // 2
                
                if row[mid] > row[mid + 1] and row[mid] > row[mid - 1] and row[mid] > newMat[i + 1][mid] and row[mid] > newMat[i - 1][mid]:
                    return [i - 1, mid - 1]

                elif row[mid] < row[mid + 1]:
                    left = mid

                else:
                    right = mid

            return [-2, -2]

        newMat = [[-1] * (len(mat[0]) + 2)]
        for row in mat:
            newMat.append([-1] + row + [-1])

        newMat.append([-1] * (len(mat[0]) + 2))

        i = 1

        for row in newMat[1:-1]:
            result = binarySearch(i, row)
            if result[0] != -2:
                return result 
            i +=1

        return [1, 1]