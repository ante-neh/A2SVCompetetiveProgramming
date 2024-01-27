class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        result = [0] * len(pref)

        for i in range(1, len(pref)):
            result[i] = pref[i - 1] ^ pref[i]
        
        result[0] = pref[0]
        
        return result