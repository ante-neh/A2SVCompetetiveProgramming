class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount, tCount = Counter(s), Counter(t)
        operations = 0

        for value, freq in sCount.items():
            if freq - tCount[value] > 0:
                operations += freq - tCount[value]

        return operations