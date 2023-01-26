class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse(num):
            reversedNum = 0
            
            while num != 0:
                diff = num % 10
                reversedNum = reversedNum * 10 + diff
                num = num // 10
            
            return reversedNum
        reversedNums = set()
        
        for num in nums:
            reversedNums.add(num)
            reversedNums.add(reverse(num))
        
        return len(reversedNums)
        