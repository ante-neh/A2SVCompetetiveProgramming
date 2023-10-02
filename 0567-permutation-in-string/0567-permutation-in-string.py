class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = defaultdict(int)
        s2Count = defaultdict(int)
        left = 0
        for c in s1:
            s1Count[c] += 1

        for right in range(len(s2)):
            s2Count[s2[right]] += 1
            if right - left + 1 == len(s1):
                if s2Count == s1Count:
                    return True

                s2Count[s2[left]] -= 1
                if s2Count[s2[left]] == 0:
                    s2Count.pop(s2[left])
                
                left += 1

        return False