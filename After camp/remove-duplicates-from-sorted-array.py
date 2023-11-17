class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0

        for read in range(len(nums)):
            if nums[write] != nums[read]:
                write += 1
                nums[write] = nums[read]

        return write + 1