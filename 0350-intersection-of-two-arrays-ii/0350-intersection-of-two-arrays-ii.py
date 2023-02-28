class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = [float("inf")] * (1000 + 1)
        nums = [nums1, nums2]
        
        for num in nums:
            tempFreq = [0] * (1000 + 1)
            
            for n in num:
                tempFreq[n] += 1
                
            for i in range(len(tempFreq)):
                count[i] = min(count[i], tempFreq[i])
                
        result = []
        
        for i in range(len(count)):
            if count[i] > 0:
                while count[i] > 0:
                    result.append(i)
                    count[i] -= 1
        return result