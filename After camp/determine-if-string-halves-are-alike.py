class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a','e','i','o','u', 'A', 'E', 'I','O','U'])
        leftCount, rightCount = 0, 0
        half = len(s) // 2

        for i in range(len(s)):
            if i < half:
                if s[i] in vowels:
                    leftCount += 1
            
            else:
                if s[i] in vowels:
                    rightCount += 1

        return leftCount == rightCount