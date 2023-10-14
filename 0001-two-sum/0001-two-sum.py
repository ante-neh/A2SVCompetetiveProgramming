class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToIndexPair = defaultdict(int)

        for i in range(len(nums)):
            if target - nums[i] in valueToIndexPair:
                return [valueToIndexPair[target - nums[i]], i]

            valueToIndexPair[nums[i]] = i

            