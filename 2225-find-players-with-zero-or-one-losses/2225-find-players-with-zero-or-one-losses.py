class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossFreq, winnerFreq = {}, {}
        
        for i in range(len(matches)):
            lossFreq[matches[i][1]] = 1 + lossFreq.get(matches[i][1], 0)
        lossers = []
        for item in lossFreq.items():
            if item[1] == 1:
                lossers.append(item[0])
        
        for i in range(len(matches)):
            if not matches[i][0] in lossFreq.keys():
                winnerFreq[matches[i][0]] = 1 + winnerFreq.get(matches[i][0], 0)
                
        winners = []
        
        for item in winnerFreq.items():
            winners.append(item[0])
            
        lossers, winners = sorted(lossers), sorted(winners)
        
        answer = [[]] * 2
        
        answer[0], answer[1]= winners, lossers
        
        return answer
        
            
                
        