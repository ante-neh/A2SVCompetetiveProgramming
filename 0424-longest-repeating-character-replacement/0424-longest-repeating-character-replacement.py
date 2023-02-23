class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLen = 1
        sCount = {}
        maxFreq = 0
        for right in range(len(s)):
            sCount[s[right]] = 1 + sCount.get(s[right], 0)
            maxFreq = max(maxFreq, sCount[s[right]])
            while (right - left + 1) - maxFreq > k:
                sCount[s[left]] -= 1
                left += 1
                
            maxLen = max(maxLen, right - left + 1)
            
        return maxLen