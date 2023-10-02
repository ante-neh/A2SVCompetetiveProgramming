class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        left = 0
        sCount = defaultdict(int)

        for right in range(len(s)):
            sCount[s[right]] += 1
            while right - left + 1 - max(sCount.values()) > k:
                sCount[s[left]] -= 1
                if sCount[s[left]] == 0:
                    sCount.pop(s[left])

                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength
