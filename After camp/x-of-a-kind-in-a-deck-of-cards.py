class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deckFreq = Counter(deck)
        maxFreq = max(deckFreq.values())

        for x in range(2, maxFreq + 1):
            flag = False
            for item in deckFreq.items():
                if item[1] % x:
                    flag = True
                    break

            if not flag:
                return True

        return False

            