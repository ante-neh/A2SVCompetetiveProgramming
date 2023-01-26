class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reversedNums = set()
        
        for num in nums:
            reversedNums.add(num)
            reversedNums.add(int(str(num)[::-1]))
        
        return len(reversedNums)
        