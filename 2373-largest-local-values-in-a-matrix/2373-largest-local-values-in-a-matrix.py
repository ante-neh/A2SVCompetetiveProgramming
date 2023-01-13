class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, i = len(grid), 0
        maxLocal = [[0] * (n-2) for _ in range(n-2)]
        
        for r in range(n-2):
            for c in range(n-2):
                tempMax = 0
                for k in range(r, r+3):
                    for j in range(c, c+3):
                        tempMax = max(tempMax, grid[k][j])
                maxLocal[i // (n-2)][i % (n-2)] = tempMax
                i += 1
        return maxLocal