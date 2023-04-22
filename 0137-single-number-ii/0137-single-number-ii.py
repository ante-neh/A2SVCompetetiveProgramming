class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = 0
        seen_twice = 0
        for n in nums:
            seen_once, seen_twice = seen_once ^ seen_twice | seen_once ^ n, seen_once & (~(seen_twice ^ (~n)))
        return seen_once