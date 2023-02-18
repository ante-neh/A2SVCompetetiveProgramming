class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        numsFreq = {}
        
        for num in nums:
            numsFreq[num] = 1 + numsFreq.get(num, 0)
        
        sumOfUniqueElement = 0
        
        for val, freq in numsFreq.items():
            if freq == 1:
                sumOfUniqueElement += val
                
        return sumOfUniqueElement