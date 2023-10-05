class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sCount = defaultdict(int)
        left = 0
        maxLength = 0

        for right in range(len(s)):
            sCount[s[right]] += 1
            while max(sCount.values()) > 1:
                sCount[s[left]] -= 1
                if sCount[s[left]] == 0:
                    sCount.pop(s[left])

                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength
