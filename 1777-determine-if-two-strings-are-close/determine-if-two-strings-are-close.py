class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        wordOneCounter, wordTwoCounter = Counter(word1), Counter(word2)

        freqOne, freqTwo = list(wordOneCounter.values()), list(wordTwoCounter.values())

        p1, p2 = 0, 0
        freqOne.sort()
        freqTwo.sort()

        while p1 < len(freqOne) and p2 < len(freqTwo):
            if freqOne[p1] != freqTwo[p2]:
                return False

            p1, p2 = p1 + 1, p2 + 1

        return p1 == len(freqOne) and p2 == len(freqTwo) and set(word1) == set(word2)
        