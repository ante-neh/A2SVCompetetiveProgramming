class Solution:
    def countHomogenous(self, s: str) -> int:
        sCount = defaultdict(int)
        left = 0
        numberOfHomogenousSubstrings = 0
        mod = (10 ** 9) + 7

        for right in range(len(s)):
            sCount[s[right]] += 1

            while len(sCount) > 1:
                sCount[s[left]] -= 1
                if sCount[s[left]] == 0:
                    sCount.pop(s[left])

                left += 1

            numberOfHomogenousSubstrings += right - left + 1

        return numberOfHomogenousSubstrings % mod