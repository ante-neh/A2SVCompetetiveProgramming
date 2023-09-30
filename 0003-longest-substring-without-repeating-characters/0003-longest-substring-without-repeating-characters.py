class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sCount = {}
        maxLen = 0
        left = 0
        
        for right in range(len(s)):
            sCount[s[right]] = 1 + sCount.get(s[right], 0)
            while max(sCount.values()) > 1:
                sCount[s[left]] -= 1
                if sCount[s[left]] == 0:
                    sCount.pop(s[left])
                
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen