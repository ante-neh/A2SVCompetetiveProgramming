class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiralArray = []
        
        top, left = 0, 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        while True:
            if left > right:
                break

            for i in range(left, right + 1):
                spiralArray.append(matrix[top][i])
            top += 1

            if top > bottom:
                break

            for i in range(top, bottom + 1):
                spiralArray.append(matrix[i][right])
            right -= 1

            if left > right:
                break

            for i in range(right, left - 1, -1):
                spiralArray.append(matrix[bottom][i])
            bottom -= 1

            if top > bottom:
                break

            for i in range(bottom, top - 1, -1):
                spiralArray.append(matrix[i][left])
            left += 1
                
        return spiralArray