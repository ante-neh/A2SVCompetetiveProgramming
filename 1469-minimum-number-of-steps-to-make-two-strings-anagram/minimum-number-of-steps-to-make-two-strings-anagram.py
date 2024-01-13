class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount, tCount = Counter(s), Counter(t)

        def count(str1, str2, count1, count2):
            counter = 0
            for c in str1:
                counter += count1[c] - count2[c] if count1[c] >= count2[c] else 0

            return counter

        return min(count(list(set(s)), list(set(t)), sCount, tCount), count(list(set(t)), list(set(s)), tCount, sCount))