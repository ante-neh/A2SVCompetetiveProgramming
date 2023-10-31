class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valToIndexPair = {}

        for i in range(len(nums)):
            if target - nums[i] in valToIndexPair:
                return [valToIndexPair[target - nums[i]], i]

            valToIndexPair[nums[i]] = i

            