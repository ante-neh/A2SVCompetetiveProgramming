class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        minLength = float("inf")
        minSubString = ""
        tCount, sCount = defaultdict(int), defaultdict(int)
        for c in t:
            tCount[c] += 1

        have, need = 0, len(tCount)
            
        for right in range(len(s)):
            sCount[s[right]] += 1
            
            if s[right] in tCount and sCount[s[right]] == tCount[s[right]]:
                have += 1

            while have == need:
                if right - left + 1 < minLength:
                    minSubString = s[left:right + 1]
                    minLength = right - left + 1

                sCount[s[left]] -= 1

                if s[left] in tCount and sCount[s[left]] < tCount[s[left]]:
                    have -= 1

                left += 1

        return minSubString


