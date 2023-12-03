class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(row):
            left, right = -1, len(row)
            while left + 1 < right:
                mid = left + (right - left) // 2
                if row[mid] == target:
                    return True

                elif row[mid] > target:
                    right = mid
                
                else:
                    left = mid

            return False

        left, right = -1, len(matrix)

        while left + 1 < right:
            mid = left + (right - left) // 2
            if target <= matrix[mid][-1] and target >= matrix[mid][0]:
                return binarySearch(matrix[mid])

            elif target > matrix[mid][-1]:
                left = mid

            elif target < matrix[mid][0]:
                right = mid



            