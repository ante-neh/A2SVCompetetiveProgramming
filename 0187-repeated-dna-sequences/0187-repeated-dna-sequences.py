class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sCount = defaultdict(int)
        left = 0
        result = set()

        for right in range(len(s)):
            if right - left + 1 == 10:
                sCount[s[left:left + 10]] += 1
                left += 1
        
        for item in sCount.items():
            if item[1] > 1:
                result.add(item[0])

        return result