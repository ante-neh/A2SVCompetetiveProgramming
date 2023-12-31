class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxLen = 0
        charIndex = {}

        for i in range(len(s)):
            if s[i] in charIndex:
                maxLen = max(maxLen, i - charIndex[s[i]] - 1)
                
            else:
                charIndex[s[i]] = i

        return maxLen if len(charIndex) != len(s) else -1