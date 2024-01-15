class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winnersFreq, losersFreq = defaultdict(int), defaultdict(int)

        for winner, loser in matches:
            winnersFreq[winner] += 1
            losersFreq[loser] += 1

        winners, losers = [], []
        for winner, loser in matches:
            if losersFreq[loser] == 1:
                losers.append(loser)
            
            if losersFreq[winner] == 0:
                winners.append(winner)

        winners = sorted(set(winners))
        losers = sorted(set(losers))

        return [winners, losers]


        