class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a','e','i','o','u'])
        left = 0
        maxNumberOfVowel = 0
        curCount = 0

        for right in range(len(s)):
            if s[right] in vowels:
                curCount += 1

            if right - left + 1 == k:
                maxNumberOfVowel = max(maxNumberOfVowel, curCount)
                if s[left] in vowels:
                    curCount -= 1

                left += 1

        return maxNumberOfVowel
