class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            if b == 0:
                return a

            return gcd(b, a % b)
        
        deckCount = {}
        for d in deck:
            deckCount[d] = 1 + deckCount.get(d, 0)
            
        value = []
        for item in deckCount.items():
            value.append(item[1])
        cur = value[0]
        for i in range(1, len(value)):
            cur = gcd(max(cur, value[i]), min(cur, value[i]))
            
        return cur >= 2