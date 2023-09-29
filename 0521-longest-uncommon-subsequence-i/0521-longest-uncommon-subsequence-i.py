class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        def isSubsequence(word1, word2):
            p1, p2 = 0, 0

            while p1 < len(word1) and p2 < len(word2):
                if word1[p1] == word2[p2]:
                    p1 += 1

                p2 += 1

            return p1 == len(word1)

        if len(a) > len(b) and not isSubsequence(a, b):
            return len(a)
        
        elif len(b) >= len(a) and not isSubsequence(b, a):
            return len(b)
        
        else:
            return -1