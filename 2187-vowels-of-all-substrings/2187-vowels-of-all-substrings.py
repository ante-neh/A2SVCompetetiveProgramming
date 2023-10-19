class Solution:
    def countVowels(self, word: str) -> int:
        vows = set("aeiou")
        l = len(word)
        s = 0
        for i in range(l):
            if word[i] in vows:
                s += (i + 1) * (l - i)
        return s