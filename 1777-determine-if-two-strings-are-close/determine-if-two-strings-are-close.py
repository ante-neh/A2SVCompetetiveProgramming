class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        wordOneCounter, wordTwoCounter = Counter(word1), Counter(word2)
        freqOne, freqTwo = list(wordOneCounter.values()), list(wordTwoCounter.values())
        freqOne.sort()
        freqTwo.sort()

        return freqOne == freqTwo and set(word1) == set(word2)
        