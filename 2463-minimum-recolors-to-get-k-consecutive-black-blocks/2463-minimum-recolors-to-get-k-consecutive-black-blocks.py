class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whiteCount = defaultdict(int)
        left = 0
        count = 0
        minimumRecolors = float("inf")

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                whiteCount[blocks[right]] += 1

            if right - left + 1 == k:
                minimumRecolors = min(minimumRecolors, whiteCount['W'])
                whiteCount[blocks[left]] -= 1

                if whiteCount[blocks[left]] == 0:
                    whiteCount.pop(blocks[left])
                
                left += 1

        return minimumRecolors