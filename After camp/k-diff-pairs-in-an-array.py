class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        visited = set()
        visited.add(float("inf"))

        for index, num in enumerate(nums):
            result = self.binarySearch(nums, num + k)
            if result[0] != float("inf") and (result[0], num) not in visited and result[1] != index:
                count += 1
                visited.add((result[0], num))

        return count 

    def binarySearch(self,nums, target):
        left, right = -1, len(nums)

        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return [nums[mid], mid]
            
            elif nums[mid] > target:
                right = mid

            else:
                left = mid

        return [float("inf"), float("inf")]