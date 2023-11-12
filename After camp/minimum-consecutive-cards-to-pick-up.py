class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        cardsFreq = set()
        left = 0
        minLength = float("inf")

        for right in range(len(cards)):
            while cards[right] in cardsFreq:
                minLength = min(minLength, right - left + 1)
                cardsFreq.remove(cards[left])
                left += 1
                
            cardsFreq.add(cards[right])

        return -1 if minLength == float("inf") else minLength