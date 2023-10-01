class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        sCount = defaultdict(int)
        left = 0
        count = 0

        for right in range(len(s)):
            sCount[s[right]] += 1
            if right - left + 1 == 3:
                if len(sCount) == 3:
                    count += 1
                sCount[s[left]] -= 1

                if sCount[s[left]] == 0:
                    sCount.pop(s[left])
                left += 1

        return count
