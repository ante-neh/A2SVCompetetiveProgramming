class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pIndex, nIndex = 0, 1
        modifiedNums = [0] * len(nums)
        
        for num in nums:
            if num > 0:
                modifiedNums[pIndex] = num
                pIndex += 2
                
            else:
                modifiedNums[nIndex] = num
                nIndex += 2
                
        return modifiedNums
                
                
            