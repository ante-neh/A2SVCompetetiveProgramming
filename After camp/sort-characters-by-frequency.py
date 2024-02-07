class Solution:
    def frequencySort(self, s: str) -> str:
        charFreq = Counter(s)
        charFreq = sorted(charFreq.items(), key=lambda item:item[1], reverse = True)
        result = ""
        for items in charFreq:
            result += items[0] * items[1]

        return result