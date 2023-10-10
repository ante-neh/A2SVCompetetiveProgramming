class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumRemainderPair = defaultdict(int)
        sumRemainderPair[0] = -1
        curSum = 0

        for right in range(len(nums)):
            curSum += nums[right]
            if curSum % k in sumRemainderPair and right - sumRemainderPair[curSum % k] > 1:
                return True
            if curSum % k not in sumRemainderPair:
                sumRemainderPair[curSum % k] = right

        return False
