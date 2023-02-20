class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numsFreq = {}
        
        for i in range(len(arr)):
            numsFreq[arr[i]] = 1 + numsFreq.get(arr[i], 0)
            
        return True if len(numsFreq.values()) == len(set(numsFreq.values())) else False
        
        
            
        
        