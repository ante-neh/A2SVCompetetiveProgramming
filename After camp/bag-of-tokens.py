class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if not tokens or power < tokens[0]: return 0
        l,r=0,len(tokens)-1
        curScore,maxScore=0,0
        while l<=r:
            if power>=tokens[l]:
                curScore+=1
                power-=tokens[l]
                l+=1
            else:
                curScore-=1
                power+=tokens[r]
                r-=1
            maxScore=max(curScore,maxScore)
        return maxScore
            