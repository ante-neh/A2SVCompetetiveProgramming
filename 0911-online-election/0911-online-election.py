class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.winner = [0] * len(persons)
        freqCount = {}
        
        for i in range(len(persons)):
            freqCount[persons[i]] = 1 + freqCount.get(persons[i],0)
            
            if max(freqCount.values()) > freqCount[persons[i]]:
                self.winner[i] = self.winner[i - 1] 
            else:
                self.winner[i] = persons[i]
        
    def q(self, t: int) -> int:        
        left, right = -1, len(self.times)
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid
        
        return self.winner[left]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)