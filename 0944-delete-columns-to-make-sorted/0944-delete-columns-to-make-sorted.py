class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for c in range(len(strs[0])):
            for r in range(len(strs) - 1):
                if strs[r][c] > strs[r + 1][c]:
                    count += 1
                    break

        return count