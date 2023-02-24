class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        diffCount = {0:1}
        count = 0
        curSum = 0
        
        for num in nums:
            curSum += num
            diff = curSum - k
            if diff in diffCount:
                count += diffCount[diff]
            diffCount[curSum] = 1 + diffCount.get(curSum, 0)
            
            
        return count 