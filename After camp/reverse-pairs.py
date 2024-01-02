class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.pairs = 0
        def mergeSort(nums):
            if len(nums) < 2:
                return nums

            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            
            return self.merge(left, right)

        mergeSort(nums)

        return self.pairs

    def merge(self, nums1, nums2):
        for num in nums1:
            index = bisect_left(nums2, num / 2)
            self.pairs += index
        
        result = nums1 + nums2
        result.sort()

        return result