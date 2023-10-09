class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sumRemaindarPair = defaultdict(int)
        sumRemaindarPair[0] = 1
        curSum = 0
        count = 0

        for i in range(len(nums)):
            curSum += nums[i]
            if curSum % k in sumRemaindarPair:
                count += sumRemaindarPair[curSum % k]

            sumRemaindarPair[curSum % k] += 1

        return count