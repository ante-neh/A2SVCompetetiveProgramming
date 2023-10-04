from collections import defaultdict
class Solution:
    def KLengthSubstringsWithNoRepeatedCharacters(self,s, k):
        sCount = defaultdict(int)
        count = 0
        left = 0

        for right in range(len(s)):
            sCount[s[right]] += 1

            if right - left + 1 == k:
                if max(sCount.values()) == 1:
                    count += 1
                print(sCount)
                sCount[s[left]] -= 1

                if sCount[s[left]] == 0:
                    sCount.pop(s[left])
                
                left += 1

        return count
    