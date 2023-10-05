class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        curSum = sum(nums[:k + 1])
        left = 0
        cur = k
        result = [-1] * len(nums)
        if k == 0:
            return nums

        for right in range(k + 1, len(nums)):
            curSum += nums[right]
            if right - left == 2 * k:
                result[cur] = curSum // ((2 * k) + 1)
                curSum -= nums[left]
                left += 1
                cur += 1

        return result
