class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a','e','i','o','u', 'A', 'E', 'I','O','U'])
        leftCount, rightCount = 0, 0
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] in vowels:
                leftCount += 1
            if s[right] in vowels:
                rightCount += 1

            left += 1
            right -= 1

        return leftCount == rightCount