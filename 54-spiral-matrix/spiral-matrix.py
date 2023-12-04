class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]: 
        spiralMatrix = []
        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        iteration = True

        while True:
            if left > right:
                break
                
            for i in range(left, right + 1):
                spiralMatrix.append(matrix[top][i])

            top += 1
            if top > bottom:
                break

            for i in range(top, bottom + 1):
                spiralMatrix.append(matrix[i][right])

            right -= 1
            if left > right:
                break

            for i in range(right, left - 1, -1):
                spiralMatrix.append(matrix[bottom][i])

            bottom -= 1
            if top > bottom:
                break

            for i in range(bottom, top - 1, -1):
                spiralMatrix.append(matrix[i][left])

            left += 1

        return spiralMatrix