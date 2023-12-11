class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        numFreq = defaultdict(int)

        for num in arr:
            numFreq[num] += 1

        for val, freq in numFreq.items():
            if freq / len(arr) > 0.25:
                return val

            