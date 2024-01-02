class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numsFreq = defaultdict(int)
        for num in nums:
            numsFreq[num] += 1
        
        result = [[] for _ in range(max(numsFreq.values()))]

        for num in nums:
            while numsFreq[num] != 0:
                result[numsFreq[num] - 1].append(num)
                numsFreq[num] -= 1
            
            numsFreq.pop(num)

        return result