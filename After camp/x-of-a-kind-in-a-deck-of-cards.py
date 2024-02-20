class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deckFreq = Counter(deck)
        x = 0
        for val in deckFreq.values():
            x = self.gcd(max(val, x), min(val, x))

        return x > 1

    def gcd(self, a, b):
        if b == 0:
            return a

        return self.gcd(b, a % b)
            