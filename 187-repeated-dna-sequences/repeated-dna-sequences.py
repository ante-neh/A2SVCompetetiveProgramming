class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        subArrayFreq = defaultdict(int)
        result = set()
        left = 0

        for right in range(len(s)):
            if right - left + 1 == 10:
                subArrayFreq[s[left:right + 1]] += 1
                if subArrayFreq[s[left:right + 1]] > 1:
                    result.add(s[left:right + 1])

                left += 1

        return result