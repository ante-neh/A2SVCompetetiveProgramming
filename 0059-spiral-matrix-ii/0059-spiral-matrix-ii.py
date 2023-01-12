class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [i for i in range(1,(n**2) + 1)]
        top, left = 0, 0
        right = n - 1
        bottom = n - 1
        spiralMatrix = [[0 for i in range(n)] for i in range(n)]
        index = 0
        
        
        while True:
            if left > right:
                break

            for i in range(left, right + 1, 1):
                spiralMatrix[top][i] = nums[index]
                index += 1

            top += 1

            if top > bottom:
                break

            for i in range(top, bottom + 1, 1):
                spiralMatrix[i][right] = nums[index]
                index += 1
            right -= 1

            if left > right:
                break

            for i in range(right, left - 1, -1):
                spiralMatrix[bottom][i] = nums[index]
                index += 1

            bottom -= 1

            if top > bottom:
                break

            for i in range(bottom, top - 1, -1):
                spiralMatrix[i][left] = nums[index]
                index += 1

            left += 1
            
        return spiralMatrix