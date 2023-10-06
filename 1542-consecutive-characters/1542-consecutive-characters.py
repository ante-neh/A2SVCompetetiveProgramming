class Solution:
    def maxPower(self, s: str) -> int:
        sCount = defaultdict(int)
        left = 0
        power = 0

        for right in range(len(s)):
            sCount[s[right]] += 1

            while len(sCount) > 1:
                sCount[s[left]] -= 1
                if sCount[s[left]] == 0:
                    sCount.pop(s[left])

                left += 1

            power = max(power, right - left + 1)

        return power