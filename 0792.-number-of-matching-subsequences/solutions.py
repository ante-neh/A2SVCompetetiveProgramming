class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        visited = set()
        invalid = set()
        numberOfMatching = 0

        def isSubsequence(word):
            i, j = 0, 0 

            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1

            return i == len(word)

        for word in words:
            if word in visited:
                numberOfMatching += 1
            elif word in invalid:
                continue

            else:
                if isSubsequence(word):
                    visited.add(word)
                    numberOfMatching += 1

                else:
                    invalid.add(word)

        return numberOfMatching