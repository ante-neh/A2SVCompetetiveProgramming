class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrFreq = Counter(arr)

        return len(arrFreq.values()) == len(set(arrFreq.values()))