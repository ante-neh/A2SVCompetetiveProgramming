class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whiteCount = 0
        left = 0
        minimumRecolors = float("inf")

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                whiteCount += 1

            if right - left + 1 == k:
                minimumRecolors = min(minimumRecolors, whiteCount)
                if blocks[left] == 'W':
                    whiteCount -= 1

                left += 1

        return minimumRecolors