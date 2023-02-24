class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sCount = set()
        maxLen, l = 0, 0
        
        for r in range(len(s)):
            while s[r] in sCount:
                sCount.remove(s[l])
                l += 1
            sCount.add(s[r])
            maxLen = max(maxLen, r - l + 1)
            
        return maxLen