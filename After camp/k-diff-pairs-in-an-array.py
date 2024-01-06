class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        visited = set()
        visited.add(float("inf"))

        for index, num in enumerate(nums):
            result1, result2 = self.binarySearch(nums, num - k), self.binarySearch(nums, num + k)
            if (result1[0] not in visited and result1[1] != index)  or (result2[0] not in visited and result2[1] != index):
                count += 1
                visited.add(result1[0])
                visited.add(result2[0])
                visited.add(num)

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