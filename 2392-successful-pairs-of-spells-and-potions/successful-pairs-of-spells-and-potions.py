class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        def binarySearch(mid):
            left = bisect_left(potions, ceil(success / mid))
            return len(potions) - left

        result = []

        for num in spells:
            result.append(binarySearch(num))

        return result