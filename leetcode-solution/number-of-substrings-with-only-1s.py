class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        numberOfOnes = 0
        left = 0
        mod = (10 ** 9) + 7

        for right in range(len(s)):
            if s[right] == '0':
                count += 1

            while count > 0:
                if s[left] == '0':
                    count -= 1

                left += 1

            numberOfOnes += right - left + 1

        return numberOfOnes % mod
