class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sCount, pCount = {}, {}
        left = 0

        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            

        result = []

        for right in range(len(s)):
            sCount[s[right]] = 1 + sCount.get(s[right], 0)
            if right - left + 1 == len(p):
                if sCount == pCount:
                    result.append(left)

                sCount[s[left]] -= 1

                if sCount[s[left]] == 0:
                    sCount.pop(s[left])

                left += 1

        return result

            
        


        