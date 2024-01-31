class Solution:
    def maxProduct(self, words: List[str]) -> int:
        states = [0] * len(words)
        maxProduct = 0

        for i in range(len(words)):
            for c in words[i]:
                states[i] |= (1 << (ord(c) - ord('a')))

            for j in range(i):
                if not states[i] & states[j]:
                    maxProduct = max(maxProduct, len(words[i]) * len(words[j]))

        return maxProduct 