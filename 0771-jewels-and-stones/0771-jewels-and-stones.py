class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stonesFreq = {}
        
        for stone in stones:
            stonesFreq[stone] = 1 + stonesFreq.get(stone, 0)
            
        count = 0
        
        for c in jewels:
            if c in stonesFreq:
                count += stonesFreq[c]
        
        return count