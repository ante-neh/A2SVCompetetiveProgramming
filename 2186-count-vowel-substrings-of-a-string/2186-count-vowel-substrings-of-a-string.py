class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowel = set(['a','e','i','o','u'])
        count = 0

        for right in range(len(word)):
            for j in range(right + 1, len(word)):
                if set(word[right:j + 1]) == vowel:
                    count += 1

        return count
