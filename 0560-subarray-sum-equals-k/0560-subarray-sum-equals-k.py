class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumDifferencePair = defaultdict(int)
        sumDifferencePair[0] = 1
        count = 0
        curSum = 0

        for right in range(len(nums)):
            curSum += nums[right]
            if curSum - k  in sumDifferencePair:
                count += sumDifferencePair[curSum - k]

            sumDifferencePair[curSum] += 1
          
        return count 