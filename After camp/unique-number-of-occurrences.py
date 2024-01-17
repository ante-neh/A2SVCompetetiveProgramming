class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrFreq = Counter(arr)
        freq = list(arrFreq.values())
        freq.sort()

        for i in range(1, len(freq)):
            if freq[i] == freq[i - 1]:
                return False

        return True