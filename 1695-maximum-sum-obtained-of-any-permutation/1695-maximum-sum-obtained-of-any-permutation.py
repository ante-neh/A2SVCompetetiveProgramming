class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse = True)
        maxPermutationSum = 0
        lastEnd = 0
        modulo = 10 ** 9 + 7

        for request in requests:
            lastEnd = max(lastEnd, request[1])

        prefixSum = [0] * (len(nums) + 1)

        for start, end in requests:
            prefixSum[start] += 1
            prefixSum[end + 1] -= 1

        
        for i in range(1, len(prefixSum)):
            prefixSum[i] += prefixSum[i - 1]

        
        prefixSum.sort(reverse = True)

        for i in range(len(nums)):
            maxPermutationSum += nums[i] * prefixSum[i]

        return maxPermutationSum % modulo
        