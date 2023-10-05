class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numsCount = Counter(nums)
        result = set()

        for num in nums:
            if numsCount[num] > len(nums) // 3:
                result.add(num)

        return result